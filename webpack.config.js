var path = require("path")
var webpack = require("webpack")

module.exports = {
  mode: "development",
  context: __dirname,
  entry: "./techmeet/static/app/index",
  devtool: "cheap-module-eval-source-map",
  output: {
    path: path.resolve(__dirname, "techmeet/static/bundles"),
    filename: "[name].js",
    publicPath: "http://localhost:3000/",
  },
  devServer: {
    publicPath: "http://localhost:3000/",
    hot: true,
    port: "3000",
    host: "0.0.0.0",
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    proxy: {
      '**': {
        target: 'http://backend:8000',
        headers: {
          'X-From-Webpack': true,
        },
      }
    },
    overlay: true,
    stats: "minimal",
  },
  module: {
    rules: [
      {
        test: /\.m?jsx?$/,
        include: path.resolve(__dirname, "techmeet/static/app"),
        loaders: ["babel-loader"],
      },
      {
        test: /\.css$/,
        loaders: ["style-loader", "css-loader"],
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: ["file-loader"],
      },
    ],
  },
  plugins: [new webpack.HotModuleReplacementPlugin()],
  resolve: {
    modules: ["node_modules"],
    extensions: [".js", ".jsx"],
  },
  stats: "minimal",
}
