const path = require('path');

module.exports = {
    entry: './assets/index.js',
    output: {
        filename: "index-bundle.js",
        path: path.resolve(__dirname,"./song_directory/static/song_directory")
    },
    entry: './assets/base_imports.js',
    output: {
        filename: "base_imports.js",
        path: path.resolve(__dirname,"./song_directory/static/song_directory")
    },
};
