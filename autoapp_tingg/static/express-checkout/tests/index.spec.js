
import * as library from '../src/index.js';
import { CHECKOUT_URL_QUERY_PARAMS, INVALID_CHECKOUT_PAYLOAD } from '../src/constants';

describe('src/index.js', () => {
    describe('handleMerchantRequest()', () => {
        //base case
        it(`validates presence of ${CHECKOUT_URL_QUERY_PARAMS}`, () => {
            HTMLFormElement.prototype.submit = jest.fn();
            expect(() => library.handleMerchantRequest({ merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: "modal" })).not.toThrow();
            expect(() => library.handleMerchantRequest({ merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: "redirect" })).not.toThrow();
        });

        //variations
        [
            {
                expectation: `params`,
                variation: { checkoutType: 'redirect', merchantProperties: { accessKey: 'asdf', countryCode: 'KE' } },
                tag: `throws error: called with { checkoutType: 'redirect', merchantProperties: { accessKey: 'asdf', countryCode: 'KE' } }`
            },
            {
                expectation: `params`,
                variation: { checkoutType: 'redirect', merchantProperties: { param: 'qwertyuiop', accessKey: 'asdf', countryCode: 'KE' } },
                tag: `throws error: called with { checkoutType: 'redirect', merchantProperties: { param: 'qwertyuiop', accessKey: 'asdf', countryCode: 'KE' } }`
            },
            {
                expectation: `accessKey`,
                variation: { checkoutType: 'redirect', merchantProperties: { params: 'qwertyuiop', countryCode: 'KE' } },
                tag: `throws error: called with { checkoutType: 'redirect', merchantProperties: { params: 'qwertyuiop', countryCode: 'KE' } }`
            },
            {
                expectation: `countryCode`,
                variation: { checkoutType: 'redirect', merchantProperties: { params: 'qwertyuiop', accessKey: 'asdf' } },
                tag: `throws error: called with { checkoutType: 'redirect', merchantProperties: { params: 'qwertyuiop', accessKey: 'asdf' } }`
            },
            {
                variation: { checkoutType: 'redirect', merchantProperties: {} },
                expectation: `params, accessKey, countryCode`,
                tag: `throws error: called with { checkoutType: 'redirect', merchantProperties: {} }`
            }
        ]
        .forEach(testCase => {
            it(testCase.tag, () => {
                expect(() => library.handleMerchantRequest(testCase.variation)).toThrowError(`${INVALID_CHECKOUT_PAYLOAD} ${testCase.expectation}`);
            });
        });
    });

    describe('renderModal()', () => {
        //base case
        it(`unhides the iframe modal, and sets its src attribute`, () => {
            document.body.innerHTML += `<iframe id='tingg-express-checkout-iframe'></iframe>`;
            library.renderModal({ merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, type: 'modal' });

            const queryParams = document.querySelector('#tingg-express-checkout-iframe').getAttribute('src');
            expect(/(params=(.+?))&(accessKey=(.+?))&(countryCode=[A-z]{2})/.test(queryParams.slice(queryParams.indexOf('?')+1))).toBeTruthy();
        });
    });
});