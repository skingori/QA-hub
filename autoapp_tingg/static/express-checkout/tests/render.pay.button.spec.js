
import Tingg from '../src/index';
import { BUTTON_COLORS, NO_BUTTON_OPTIONS_ERROR, NO_CLASS_NAME_ERROR, BUTTON_TEXT_CHARACTER_LIMIT } from '../src/constants';

const rgbToHex = rgb => {
    rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    const hex = x => ("0" + parseInt(x).toString(16)).slice(-2);

    return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
}

describe('Tingg library', () => {
    describe('renderPayButton()', () => {
        describe('param existence', () => {
            //base
            it('throws error: called with empty params', () => {
                document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
    
                expect(() => Tingg.renderPayButton()).toThrow(NO_BUTTON_OPTIONS_ERROR);
            });

            //variations
            [
                {
                    variation: null,
                    expectation: NO_BUTTON_OPTIONS_ERROR,
                    tag: `throws error: called with null`,
                },
                {
                    variation: undefined,
                    expectation: NO_BUTTON_OPTIONS_ERROR,
                    tag: `throws error: called with undefined`
                }
            ]
            .forEach(testCase => {
                it(testCase.tag, () => {
                    document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
                    expect(() => Tingg.renderPayButton(testCase.variation)).toThrow(testCase.expectation);
                });
            });
        });

        describe('className property validation', () => {
            //base
            it(`executes with: called with { className: 'jest-checkout-button' }`, () => {
                document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
                expect(() => Tingg.renderPayButton({ className: 'jest-checkout-button' })).not.toThrow(NO_CLASS_NAME_ERROR);
            });

            //variations
            [
                {
                    variation: {},
                    expectation: NO_CLASS_NAME_ERROR,
                    tag: `throws error: called with empty object`
                },
                {
                    expectation: NO_CLASS_NAME_ERROR,
                    variation: { class: 'jest-checkout-button' },
                    tag: `throws error: called with { class: 'jest-checkout-button' }`
                },
                {
                    expectation: NO_CLASS_NAME_ERROR,
                    variation: { classname: 'jest-checkout-button' },
                    tag: `throws error: called with { classname: 'jest-checkout-button' }`
                },
                {
                    expectation: NO_CLASS_NAME_ERROR,
                    variation: { class_name: 'jest-checkout-button' },
                    tag: `throws error: called with { class_name: 'jest-checkout-button' }`
                },
                {
                    expectation: NO_CLASS_NAME_ERROR,
                    variation: { id: 'jest-checkout-button' },
                    tag: `throws error: called with { id: 'jest-checkout-button' }`
                }
            ]
            .forEach(testCase => {
                it(testCase.tag, () => {
                    document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
                    expect(() => Tingg.renderPayButton(testCase.variation)).toThrow(testCase.expectation);
                });
            });
        });

        describe(`text property validation: ${BUTTON_TEXT_CHARACTER_LIMIT} character limit`, () => {
            beforeEach(() => {
                document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
            });
    
            afterEach(() => {
                document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
            });

            //base
            it(`defaults button text to 'Proceed to Payment': called with { className: 'jest-checkout-button' }`, () => {
                document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
                Tingg.renderPayButton({ className: 'jest-checkout-button' });
                expect(document.querySelector('.jest-checkout-button').textContent).toBe('Proceed to Payment');
            });

            //variations
            //create random strings of varied lengths and check for truncation
            [
                {
                    expectation: `Get "Facebook Jest" tickets now!`,
                    variation: { text: 'Get "Facebook Jest" tickets now!', className: 'jest-checkout-button' },
                    tag: `sets button text to 'Get "Facebook Jest" tickets now!': { text: 'Get "Facebook Jest" tickets now!', className: 'jest-checkout-button' }`
                },
                {
                    expectation: `Get "Facebook Jest" tickets now! 50`,
                    variation: { text: 'Get "Facebook Jest" tickets now! 50% off', className: 'jest-checkout-button' },
                    tag: `sets button text to 'Get "Facebook Jest" tickets now! 50': { text: 'Get "Facebook Jest" tickets now! 50% off', className: 'jest-checkout-button' }`
                }
            ]
            .forEach(testCase => {
                it(testCase.tag, () => {
                    Tingg.renderPayButton(testCase.variation);
                    expect(document.querySelector('.jest-checkout-button').textContent).toBe(testCase.expectation);
                });
            });
        });

        describe(`color property validation: ${Object.keys(BUTTON_COLORS).join(',')}`, () => {
            beforeEach(() => {
                document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
            });
    
            afterEach(() => {
                document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
            });

            //base
            it(`defaults button color to green(#3BD23D) : called with { className: 'jest-checkout-button' }`, () => {
                document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
                Tingg.renderPayButton({ className: 'jest-checkout-button' });
                expect(document.querySelector('.jest-checkout-button > span').style.borderColor.toUpperCase()).toBe(BUTTON_COLORS.green);
                expect(rgbToHex(document.querySelector('.jest-checkout-button > span').style.backgroundColor).toUpperCase()).toBe(BUTTON_COLORS.green);
            });

            [
                {
                    tag: 'sets button color to red',
                    expectation: BUTTON_COLORS.red,
                    variation: { color: 'red', className: 'jest-checkout-button' }
                },
                {
                    tag: 'sets button color to blue',
                    expectation: BUTTON_COLORS.blue,
                    variation: { color: 'blue', className: 'jest-checkout-button' }
                },
                {
                    tag: 'sets button color to pink',
                    expectation: BUTTON_COLORS.pink,
                    variation: { color: 'pink', className: 'jest-checkout-button' }
                },
                {
                    tag: 'sets button color to black',
                    expectation: BUTTON_COLORS.black,
                    variation: { color: 'black', className: 'jest-checkout-button' }
                },
                {
                    tag: 'sets button color to green',
                    expectation: BUTTON_COLORS.green,
                    variation: { color: 'green', className: 'jest-checkout-button' }
                },
                {
                    tag: 'sets button color to yellow',
                    expectation: BUTTON_COLORS.yellow,
                    variation: { color: 'yellow', className: 'jest-checkout-button' }
                },
                {
                    tag: 'sets button color to purple',
                    expectation: BUTTON_COLORS.purple,
                    variation: { color: 'purple', className: 'jest-checkout-button' }
                },
                {
                    tag: 'defaults button color to green',
                    expectation: BUTTON_COLORS.green,
                    variation: { color: 'tomato', className: 'jest-checkout-button' }
                },
                {
                    tag: 'defaults button color to green',
                    expectation: BUTTON_COLORS.green,
                    variation: { color: 'cornflowerblue', className: 'jest-checkout-button' }
                }
            ]
            .forEach(testCase => {
                it(`${testCase.tag}(${testCase.expectation}) : called with ${JSON.stringify(testCase.variation)}`, () => {
                    document.body.innerHTML = `<button class='jest-checkout-button'></button>`;
                    Tingg.renderPayButton(testCase.variation);

                    expect(document.querySelector('.jest-checkout-button > span').style.borderColor.toUpperCase()).toBe(testCase.expectation);
                    expect(rgbToHex(document.querySelector('.jest-checkout-button > span').style.backgroundColor).toUpperCase()).toBe(testCase.expectation);
                });
            });
        });
    });
});