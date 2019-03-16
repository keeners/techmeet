var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  mode: "development",
  context: __dirname,
  entry: "./src/index",
  devtool: "cheap-module-eval-source-map",
  output: {
    path: path.resolve(__dirname, "static/frontend/bundles"),
    filename: "[name]-[hash].js",
    publicPath: "http://localhost:3000/"
  },
  devServer: {
    publicPath: "http://localhost:3000/",
    hot: true,
    port: "3000",
    host: "0.0.0.0",
    headers: {
      "Access-Control-Allow-Origin": "*"
    },
    overlay: true,
    stats: "minimal",
  },
  module: {
    rules: [
      {
        test: /\.m?jsx?$/,
        include: path.resolve(__dirname, "src"),
        loaders: ["babel-loader"]
      },
      {
        test: /\.css$/,
        loaders: ["style-loader", "css-loader"]
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: ["file-loader"]
      }
    ]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new BundleTracker({ filename: "webpack-stats.json" })
  ],
  resolve: {
    modules: ["node_modules"],
    extensions: [".js", ".jsx"]
  },
  stats: "minimal",
};
