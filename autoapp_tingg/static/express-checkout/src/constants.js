
module.exports = {
    CHECKOUT_TYPES: [
        `modal`, 
        `redirect`
    ],
    
    CHECKOUT_URL_QUERY_PARAMS: [
        `params`,
        `accessKey`,
        `countryCode`
    ],
    
    BUTTON_COLORS: {
        red: `#F65058`,
        blue: `#6CD1EF`,
        pink: `#F984CA`,
        black: `#0D171A`,
        green: `#3BD23D`,
        yellow: `#FFC915`,
        purple: `#5D538B`
    },

    BRAND_NAME: `tingg`,
    
    NO_CHECKOUT_TYPE_ERROR: `checkoutType not provided`,
    NO_CHECKOUT_PAYLOAD_ERROR: `merchantProperties not provided`,
    NO_CHECKOUT_TYPE: `Please provide the checkout request type i.e either 'modal' or 'redirect'`,
    INVALID_CHECKOUT_TYPE: `is not a valid checkout type. It should be either 'modal' or 'redirect'`,
    NO_CHECKOUT_OPTIONS_ERROR: `No checkout options provided, refer to documentation and pass what's required`,
    
    BUTTON_TEXT_CHARACTER_LIMIT: 35,
    NON_EXISTENT_ELEMENT: `does not exist in your DOM tree`,
    INVALID_CHECKOUT_PAYLOAD: `Missing required merchantProperties property`,
    INVALID_BUTTON_TEXT_ERROR: `Button text should be a non-empty string or number`,
    NO_BUTTON_OPTIONS_ERROR: `No button options provided, refer to documentation and pass what's required`,
    NO_CLASS_NAME_ERROR: `Please provide the class name of the element you'd like to append the checkout button to`,
}