
import './style.css';

import { 
    BRAND_NAME,
    BUTTON_COLORS,
    NO_CLASS_NAME_ERROR,
    NON_EXISTENT_ELEMENT,
    INVALID_CHECKOUT_TYPE,
    NO_CHECKOUT_TYPE_ERROR,
    NO_BUTTON_OPTIONS_ERROR,
    INVALID_CHECKOUT_PAYLOAD,
    NO_CHECKOUT_PAYLOAD_ERROR,
    INVALID_BUTTON_TEXT_ERROR,
    NO_CHECKOUT_OPTIONS_ERROR,
    CHECKOUT_URL_QUERY_PARAMS,
    BUTTON_TEXT_CHARACTER_LIMIT
} from './constants';

import { 
    isCheckoutTypeValid,
    isButtonContentValid,
    isClassNameInDomElements
} from './utils';

import poweredByImage from './assets/powered-by-tingg.svg';

const configs = require('../config/config.json');

const renderPayButton = (options) => {
    if (!options) {
        throw new Error(NO_BUTTON_OPTIONS_ERROR);
    }

    if (!options.className) {
        throw new Error(NO_CLASS_NAME_ERROR);
    }

    if (!isClassNameInDomElements(options.className)) {
        throw new Error(`'${options.className}' class ${NON_EXISTENT_ELEMENT}`);
    }

    if ('text' in options) {
        if (!isButtonContentValid(options.text)) {
            throw new Error(INVALID_BUTTON_TEXT_ERROR);
        }
    }
    
    createCheckoutButton(options);
};

const createCheckoutButton = (options) => {
    const merchantButton = document.querySelector(`.${options.className}`);
    merchantButton.classList.add(`${BRAND_NAME.toLocaleLowerCase()}-express-checkout-button`);

    const merchantButtonSpanTag = document.createElement('span');
    merchantButtonSpanTag.className = `${BRAND_NAME.toLocaleLowerCase()}-express-checkout-button-text`;
    merchantButtonSpanTag.textContent = options.text ? options.text.slice(0, BUTTON_TEXT_CHARACTER_LIMIT) : 'Proceed to Payment';

    const buttonColor = BUTTON_COLORS[options.color] !== undefined ? BUTTON_COLORS[options.color] : BUTTON_COLORS.green;
    merchantButtonSpanTag.style.borderColor = merchantButtonSpanTag.style.backgroundColor = buttonColor;

    const merchantButtonImgTag = document.createElement('img');
    merchantButtonImgTag.src = poweredByImage;
    merchantButtonImgTag.className = `${BRAND_NAME.toLocaleLowerCase()}-express-checkout-button-brand`;
    merchantButtonImgTag.alt = `Powered by ${BRAND_NAME.charAt(0).toUpperCase() + BRAND_NAME.slice(1).toLocaleLowerCase()}`;

    merchantButton.appendChild(merchantButtonSpanTag);
    merchantButton.appendChild(merchantButtonImgTag);
};

/**
 * Listen for 'close events' from the child modal window.
 * @param {*} element
 * @param {*} eventHandler
 */
const modalListener = (element, eventName, eventHandler) => {
    if (element.addEventListener) {
        element.addEventListener(eventName, eventHandler, false);
    } else if (element.attachEvent) {
        element.attachEvent(`on${eventName}`, eventHandler);
    }
};

/**
 * Verify that the merchant has provided the required options.
 * Proceed to handle the merchant request upon sucessful verification.
 * @param {object} options
 */
const renderCheckout = (options) => {
    if (options === null) {
        throw new Error(NO_CHECKOUT_OPTIONS_ERROR);
    }

    if (options === undefined) {
        throw new Error(NO_CHECKOUT_OPTIONS_ERROR);
    }

    if (!options.merchantProperties) {
        throw new Error(NO_CHECKOUT_PAYLOAD_ERROR);
    }
    
    if (!options.checkoutType) {
        throw new Error(NO_CHECKOUT_TYPE_ERROR);
    }
    
    if (!isCheckoutTypeValid(options.checkoutType)) {
        throw new Error(`${options.checkoutType} ${INVALID_CHECKOUT_TYPE}`);
    } 

    handleMerchantRequest(options);
};

/**
 * Verify that the options provided by the merchant contain all the required payload properties.
 * Proceed to route the merchant request to checkout.
 * @param {object} options
 */
const handleMerchantRequest = (options) => {
    const payloadProperties = [];
    Object.keys(options.merchantProperties).map((param) => {
        payloadProperties.push(param);
    });

    // Check if there are any missing payload properties
    let missingParams = '';
    CHECKOUT_URL_QUERY_PARAMS.filter((param) => {
        const missingParam = payloadProperties.indexOf(param) === -1;
        if (missingParam) {
            missingParams += `${param}, `;
        }
    });

    if (missingParams) {
        throw new Error(`${INVALID_CHECKOUT_PAYLOAD} ${missingParams.slice(0, -2)}`);
    } else {
        checkoutRouter(options);
    }
};

/**
 * @param {object} options
 */
const checkoutRouter = (options) => {
    switch (options.checkoutType.toLowerCase()) {
    case 'modal':
        renderModal(options);
        break;
    default:
        redirectToExpress(options);
        break;
    }
};

/**
 * 
 * @param {*} options 
 */
const getEnvironment = (options) => {
    return options.test === true 
        ? 'test'
        : 'live'
}

/**
 * Open the modal window on the merchant page.
 * @param {object} options
 */
const renderModal = (options) => {
    const env = getEnvironment(options);
    const checkoutModalIframe = document.createElement('iframe');
    checkoutModalIframe.id = `${BRAND_NAME.toLocaleLowerCase()}-express-checkout-iframe`;

    checkoutModalIframe.setAttribute('scroll', 'no');
    checkoutModalIframe.setAttribute('style', 'position: fixed; top: 0; left: 0; display:none; height: 100%; width: 100%; background-color: rgba(0,0,0,0.5); z-index: 10;');
    document.body.appendChild(checkoutModalIframe);

    // Listen to message from child window
    modalListener(window, 'message', (e) => {
        if (e.origin === configs.ORIGIN_URL) {
            if (e.data === 'closeModal') {
                checkoutModalIframe.setAttribute('src', '');
                checkoutModalIframe.style.display = 'none';
            }
        }
    });
    
    checkoutModalIframe.style.display = 'block';
    checkoutModalIframe.src = `${configs[env].MODAL_CHECKOUT_URL}?params=${options.merchantProperties.params}&accessKey=${options.merchantProperties.accessKey}&countryCode=${options.merchantProperties.countryCode}`;
};

/**
 * Redirect to express checkout.
 * @param {object} options
 */
const redirectToExpress = (options) => {
    const env = getEnvironment(options);
    const form = document.createElement('form');
    form.setAttribute('method', 'GET');
    form.setAttribute('target', '_parent');
    form.setAttribute('action', configs[env].EXPRESS_CHECKOUT_URL);

    Object.keys(options.merchantProperties).map((key) => {
        const hiddenField = document.createElement('input');
        hiddenField.setAttribute('type', 'hidden');
        hiddenField.setAttribute('name', key);
        hiddenField.setAttribute('value', options.merchantProperties[key]);
        form.appendChild(hiddenField);
    });

    document.body.appendChild(form);
    form.submit();
};

export {
    handleMerchantRequest, 
    createCheckoutButton,
    redirectToExpress, 
    checkoutRouter, 
    modalListener, 
    renderModal,
    configs
};

export default {
    renderPayButton, 
    renderCheckout 
};