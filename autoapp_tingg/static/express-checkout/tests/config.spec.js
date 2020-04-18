
const environments = {
    test: {
        ORIGIN_URL: "https://beep2.cellulant.com:9212",
        MODAL_CHECKOUT_URL: "https://beep2.cellulant.com:9212/checkout/v2/modal/",
        EXPRESS_CHECKOUT_URL: "https://beep2.cellulant.com:9212/checkout/v2/express/",
    },
    live: {
        ORIGIN_URL: "https://mula.africa",
        MODAL_CHECKOUT_URL: "https://mula.africa/v2/modal/",
        EXPRESS_CHECKOUT_URL: "https://mula.africa/v2/express/"
    }
};

describe('Envrionment configs', () => {
    const configs = require(`../config/config.json`);

    Object.keys(environments).forEach(env => {
        describe(`${env} environment`, () => {
            Object.keys(environments[env]).forEach(conf => {
                test(`[${conf}] config is set`, () => {
                    expect(environments[env][conf]).toEqual(configs[env][conf]);
                });
            });
        });
    });
});

