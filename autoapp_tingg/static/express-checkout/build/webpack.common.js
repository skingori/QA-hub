
const path = require('path');

module.exports = {
    entry: './src/index.js',
    output: {
        library: 'Tingg',
        libraryTarget: 'umd',
        libraryExport: "default",
        filename: 'tingg-checkout-library.js',
        path: path.resolve(__dirname, '../dist')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'postcss-loader',
                        options: {
                            plugins: function () {
                                return [
                                    require('autoprefixer')
                                ];
                            }
                        }
                    }
                ]
            },
            {
                test: /\.(png|jp(e*)g|svg)$/i,
                use: [
                    {
                        loader: 'url-loader',
                        options: {
                            limit: 16384
                        }
                    }
                ]
            }
        ]
    }
}
