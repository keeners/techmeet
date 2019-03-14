var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  mode: "development",
  context: __dirname,
  entry: ["./src/index"],
  devtool: "cheap-module-eval-source-map",
  output: {
    path: path.resolve("./static/frontend/bundles/"),
    filename: "[name]-[hash].js",
    // TODO: replace public path with path to external docker URL
    publicPath: "http://localhost:3000/"
  },
  devServer: {
    contentBase: path.resolve("./static/frontend/bundles/"),
    hot: true,
    port: "3000",
    host: "0.0.0.0",
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
  },
  module: {
    rules: [
      // we pass the output from babel loader to react-hot loader
      {
        test: /\.jsx?$/,
        include: path.resolve("./src/"),
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
    new BundleTracker({ filename: "./webpack-stats.json" })
  ],
  resolve: {
    modules: ["node_modules"],
    extensions: [".js", ".jsx"]
  },
};
