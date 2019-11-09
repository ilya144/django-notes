const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: {
      main: path.resolve(__dirname, "./webclient/src/index.js")
    },
    output: {
      path: path.resolve(__dirname, './webclient/static/'),
      filename: 'js/[name].js'
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: 'css/[name].css',
      }),
    ],
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        },
        {
          test: /\.css$/,
          use: [{
            loader: MiniCssExtractPlugin.loader,
          },
          'css-loader',]
        },
        {
          test: /.(jpg|jpeg|png|svg)$/,
          use: ['file-loader'],
        },
      ]
    }
  };
  