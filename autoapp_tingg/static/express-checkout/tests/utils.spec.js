
import { 
    isCheckoutTypeValid,
    isButtonContentValid,
    isClassNameInDomElements
} from '../src/utils';

describe('/src/utils.js tests', () => {
    describe('isButtonContentValid()', () => {
        [
            {
                variation: '',
                expectation: false,
                tag: `returns false: called with empty string`
            },
            {
                variation: [],
                expectation: false,
                tag: `returns false: called with Array`
            },
            {
                variation: {},
                expectation: false,
                tag: `returns false: called with Object`
            },
            {
                expectation: false,
                variation: undefined,
                tag: `returns false: called with undefined`
            },
            {
                expectation: true,
                variation: 'Get tickets now!',
                tag: `returns true: called with non-empty string`
            },
            {
                variation: 9000,
                expectation: true,
                tag: `returns true: called with number`
            },
        ]
        .forEach(testCase => {
            test(testCase.tag, () => {
                expect(isButtonContentValid(testCase.variation)).toBe(testCase.expectation);
            });
        });
    });

    describe('isClassNameInDomElements()', () => {
        test(`returns false: called with empty params`, () => {
            expect(isClassNameInDomElements()).toBe(false);
        });

        [
            {
                variation: '',
                expectation: false,
                tag: `returns false: called with empty string`
            },
            {
                variation: null,
                expectation: false,
                tag: `returns false: called with null`
            },
            {
                variation: 'some-random-useful-class',
                expectation: true,
                tag: `returns true: called with a valid class`
            },
        ]
        .forEach(testCase => {
            test(testCase.tag, () => {
                document.body.innerHTML = `<span class='some-random-useful-class'></span>`;
                expect(isClassNameInDomElements(testCase.variation)).toBe(testCase.expectation);
            });
        });
    });

    describe('isCheckoutTypeValid()', () => {
        test(`returns false: called with empty params`, () => {
            expect(isCheckoutTypeValid()).toBe(false);
        });

        [
            {
                variation: '',
                expectation: false,
                tag: `returns false: called with empty string`
            },
            {
                variation: {},
                expectation: false,
                tag: `returns false: called with Object`
            },
            {
                variation: [],
                expectation: false,
                tag: `returns false: called with Array`
            },
            {
                variation: null,
                expectation: false,
                tag: `returns false: called with null`
            },
            {
                variation: 'redirect',
                expectation: true,
                tag: `returns true: called with redirect`
            },
            {
                variation: 'Redirect',
                expectation: true,
                tag: `returns true: called with Redirect`
            },
            {
                variation: 'REDIRECT',
                expectation: true,
                tag: `returns true: called with REDIRECT`
            },
            {
                variation: 'modal',
                expectation: true,
                tag: `returns true: called with modal`
            },
            {
                variation: 'Modal',
                expectation: true,
                tag: `returns true: called with Modal`
            },
            {
                variation: 'MODAL',
                expectation: true,
                tag: `returns true: called with MODAL`
            },
            {
                variation: 'MoDal',
                expectation: true,
                tag: `returns true: called with MoDal`
            },
            {
                variation: 'ReDirect',
                expectation: true,
                tag: `returns false: called with ReDirect`
            },
            {
                variation: 'Express',
                expectation: false,
                tag: `returns false: called with Express`
            },
            {
                variation: 'Express',
                expectation: false,
                tag: `returns false: called with Express`
            },
            {
                variation: 'Random',
                expectation: false,
                tag: `returns false: called with Random`
            },
            {
                variation: 'Customizable',
                expectation: false,
                tag: `returns false: called with Customizable`
            }
        ]
        .forEach(testCase => {
            test(testCase.tag, () => {
                document.body.innerHTML = `<span class='some-random-useful-class'></span>`;
                expect(isCheckoutTypeValid(testCase.variation)).toBe(testCase.expectation);
            });
        });
    });
});