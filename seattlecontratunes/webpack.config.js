const path = require('path');
const autoprefixer = require('autoprefixer');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin")

module.exports = {
    /*entry: './assets/index.js',
    output: {
        filename: "index-bundle.js",
        path: path.resolve(__dirname,"./song_directory/static/song_directory")
    },*/
    entry: './assets/base_imports.js',
    output: {
        filename: "base_imports.js",
        path: path.resolve(__dirname,"./song_directory/static/song_directory")
    },
    output: {
        filename: "base_imports.scss",
        path: path.resolve(__dirname,"./song_directory/static/song_directory")
    },
    /*plugins: [
        new MiniCssExtractPlugin({

            filename: isDevelopment ? '[name].css' : '[name].[hash].css',

            chunkFilename: isDevelopment ? '[id].css' : '[id].[hash].css'

        })
    ],  */
    
      
  
  module: {
    rules: [
      {
        test: /\.(scss)$/,
        use: [
          {
            // Adds CSS to the DOM by injecting a `<style>` tag
            loader: 'style-loader'
          },
          {
            // Interprets `@import` and `url()` like `import/require()` and will resolve them
            loader: 'css-loader'
          },
          {
            // Loader for webpack to process CSS with PostCSS
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  autoprefixer
                ]
              }
            }
          },
          {
            // Loads a SASS/SCSS file and compiles it to CSS
            loader: 'sass-loader'
          }
        ]
      }
    ]
  }


};
