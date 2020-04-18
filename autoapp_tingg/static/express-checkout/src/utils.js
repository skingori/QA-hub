
import { CHECKOUT_TYPES } from './constants';

const isButtonContentValid = (content) => {
    const isNumber = !isNaN(content) && typeof content === 'number';
    const isString = content instanceof String || typeof content === 'string';

    const isEmpty = isString ? content.trim().length === 0 : false;
    return (isNumber || isString) && !isEmpty;
}

const isClassNameInDomElements = (className) => {
    try {
        return !!document.querySelector(`.${className}`);
    } catch (error) {
        return false;
    }
}

const isCheckoutTypeValid = (param) => {
    const isString = param instanceof String || typeof param === 'string';

    const isEmpty = isString ? param.trim().length === 0 : false;
    return isString && !isEmpty ? CHECKOUT_TYPES.includes(param.toLowerCase()) : false;
}

export {
    isCheckoutTypeValid,
    isButtonContentValid,
    isClassNameInDomElements
}