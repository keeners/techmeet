var path = require("path")
var webpack = require("webpack")
var docker = process.env.VIRTUAL_ENV === "docker"
var proxyServer = docker ? "http://backend:8000" : "http://localhost:8000"

module.exports = {
  mode: "development",
  context: __dirname,
  entry: "./techmeet/static/app/index",
  devtool: "cheap-module-eval-source-map",
  output: {
    path: path.resolve(__dirname, "techmeet/static/bundles"),
    filename: "[name].js",
    publicPath: "/static/bundles/",
  },
  devServer: {
    publicPath: "/static/bundles/",
    hot: true,
    port: "3000",
    host: "0.0.0.0",
    proxy: {
      "**": proxyServer,
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
    alias: {
      "@": path.resolve(__dirname, "techmeet/static/app"),
    },
  },
  stats: "minimal",
}
