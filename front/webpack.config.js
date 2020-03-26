var path = require('path')
    // 在内存中，根�?指定的模板页�?，生成一份内存中的�?�页，同时自动把打包好的bundle注入到页面底�?
    // 如果要配�?插件，需要在导出的�?�象�?，挂载一�? plugins 节点
var htmlWebpackPlugin = require('html-webpack-plugin')
const webpack = require('webpack')
const VueLoaderPlugin = require('vue-loader/lib/plugin');
// 当以命令行形式运�? webpack �? webpack-dev-server 的时候，工具会发现，我们并没有提�? 要打�? 的文件的 入口 �? 出口文件，�?�时，他会�?�查项�?根目录中的配�?文件，并读取这个文件，就拿到了�?�出的这�? 配置对象，然后根�?这个对象，进行打包构�?
module.exports = {
    entry: path.join(__dirname, './src/main.js'), // 入口文件
    output: {
        path: path.join(__dirname, './dist'), // 输出�?�?
        filename: 'bundle.js' // 指定输出文件的名�?
    },
    mode: 'development',
    plugins: [ // 所有webpack  插件的配�?节点
        new htmlWebpackPlugin({
            template: path.join(__dirname, './src/index.html'), // 指定模板文件�?�?
            filename: 'index.html' // 设置生成的内存页面的名称
        }),
        new VueLoaderPlugin()
    ],
    module: { // 配置所有�??三方loader 模块�?
        rules: [ // �?三方模块的匹配�?�则
            { test: /\.css$/, use: ['style-loader', 'css-loader'] }, // 处理 CSS 文件�? loader
            { test: /\.less$/, use: ['style-loader', 'css-loader', 'less-loader'] }, // 处理 less 文件�? loader
            { test: /\.scss$/, use: ['style-loader', 'css-loader', 'sass-loader'] }, // 处理 scss 文件�? loader
            { test: /\.(jpg|png|gif|bmp|jpeg)$/, use: 'url-loader?limit=7631&name=[hash:8]-[name].[ext]' }, // 处理 图片�?径的 loader
            // limit 给定的值，�?图片的大小，单位�? byte�? 如果我们引用�? 图片，大于或等于给定�? limit值，则不会�??�?为base64格式的字符串�? 如果 图片小于给定�? limit 值，则会�?�?�? base64的字符串
            { test: /\.(ttf|eot|svg|woff|woff2)$/, use: 'url-loader' }, // 处理 字体文件�? loader 
            { test: /\.js$/, use: 'babel-loader', exclude: /node_modules/ }, // 配置 Babel 来转换高级的ES�?�?
            { test: /\.vue$/, use: 'vue-loader' } // 处理 .vue 文件�? loader
        ]
    },
    resolve: {
        alias: { // �?�? Vue �?导入时候的包的�?�?
            // "vue$": "vue/dist/vue.js"
        }
    }
}