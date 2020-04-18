import Tingg from '../src/index';

import { NO_CHECKOUT_OPTIONS_ERROR, NO_CHECKOUT_PAYLOAD_ERROR, NO_CHECKOUT_TYPE_ERROR, INVALID_CHECKOUT_TYPE } from '../src/constants';

describe('Tingg library', () => {
    describe('renderCheckout()', () => {
        describe('page redirect experience', () => {
            describe('param existance', () => {
                // base case
                it(`redirects to checkout page: called with { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: "redirect" }`, () => {
                    HTMLFormElement.prototype.submit = jest.fn();
                    Tingg.renderCheckout({ merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: "redirect" });

                    expect(HTMLFormElement.prototype.submit).toHaveBeenCalledTimes(1);
                    expect(() => Tingg.renderCheckout({ merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: "redirect" })).not.toThrow();
                });

                 // variation
                 [
                    {
                        variation: null,
                        expectation: NO_CHECKOUT_OPTIONS_ERROR,
                        tag: `throws error: called with null`
                    },
                    {
                        variation: undefined,
                        expectation: NO_CHECKOUT_OPTIONS_ERROR,
                        tag: `throws error: called with undefined`
                    }
                ]
                .forEach(testCase => {
                    it(testCase.tag, () => {
                        expect(() => Tingg.renderCheckout(testCase.variation)).toThrow(testCase.expectation);
                    });
                });
            });

            describe('param validation', () => {
                // base case
                it(`redirects to checkout page: called with { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: "redirect" }`, () => {
                    HTMLFormElement.prototype.submit = jest.fn();
                    Tingg.renderCheckout({ merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: "redirect" });

                    expect(HTMLFormElement.prototype.submit).toHaveBeenCalledTimes(1);
                    expect(() => Tingg.renderCheckout({ merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: "redirect" })).not.toThrow();
                });

                // variation
                [
                    {
                        variation: {},
                        expectation: NO_CHECKOUT_PAYLOAD_ERROR,
                        tag: `throws error: called with {}`
                    },
                    {
                        variation: {type: 'redirect'},
                        expectation: NO_CHECKOUT_PAYLOAD_ERROR,
                        tag: `throws error: called with {type: 'redirect'}`
                    },
                    {
                        expectation: NO_CHECKOUT_PAYLOAD_ERROR,
                        tag: `throws error: called with { checkout: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect' }`,
                        variation: { checkout: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect'}
                    },
                    {
                        expectation: NO_CHECKOUT_PAYLOAD_ERROR,
                        tag: `throws error: called with { Payload: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect' }`,
                        variation: { Payload: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect' }
                    },
                    {
                        expectation: NO_CHECKOUT_PAYLOAD_ERROR,
                        tag: `throws error: called with { merchantproperty: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect' }`,
                        variation: { merchantproperty: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect' }
                    },
                    {
                        expectation: NO_CHECKOUT_PAYLOAD_ERROR,
                        tag: `throws error: called with { merchantproperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect' }`,
                        variation: { merchantproperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect' }
                    },
                    {
                        expectation: NO_CHECKOUT_TYPE_ERROR,
                        variation: { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" } },
                        tag: `throws error: called with { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" } }`,
                    },
                    {
                        expectation: NO_CHECKOUT_TYPE_ERROR,
                        variation: { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, render: 'redirect' },
                        tag: `throws error: called with { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, render: 'redirect' }`,
                    },
                    {
                        expectation: NO_CHECKOUT_TYPE_ERROR,
                        variation: { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, Type: 'redirect' },
                        tag: `throws error: called with { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, Type: 'redirect' }`,
                    },
                    {
                        expectation: NO_CHECKOUT_TYPE_ERROR,
                        variation: { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkouttype: 'redirect' },
                        tag: `throws error: called with { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'redirect' }`,
                    },
                    {
                        expectation: `express ${INVALID_CHECKOUT_TYPE}`,
                        variation: { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'express' },
                        tag: `throws error: called with { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, type: 'express' }`,
                    },
                    {
                        expectation: `pop-up ${INVALID_CHECKOUT_TYPE}`,
                        variation: { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, checkoutType: 'pop-up' },
                        tag: `throws error: called with { merchantProperties: { params: "qwertyuiop", accessKey: "asdf", countryCode: "KE" }, type: 'pop-up' }`,
                    }
                ]
                .forEach(testCase => {
                    it(testCase.tag, () => {
                        expect(() => Tingg.renderCheckout(testCase.variation)).toThrow(testCase.expectation);
                    });
                });
            });
        });
    });
});