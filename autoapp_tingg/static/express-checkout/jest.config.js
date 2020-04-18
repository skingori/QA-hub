module.exports = {
    "clearMocks": true,
    "collectCoverage": true,
    "collectCoverageFrom": [
        "!**/node_modules/**",
        "src/*.js",
    ],
    "coverageReporters": [
        "html",
        "text-summary"
    ],
    "moduleFileExtensions": [
        "js",
        "json"
    ],
    "transform": {
        "^.+\\.js$": "<rootDir>/node_modules/babel-jest",
        ".+\\.(css|styl|less|sass|scss|png|jpg|svg|ttf|woff|woff2)$": "jest-transform-stub"
    }
};