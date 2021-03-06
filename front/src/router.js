import VueRouter from 'vue-router'
import leftBox from './component/left.vue'
import mainBox from './component/right.vue'
import query from './component/query.vue'
import renew from './component/renew.vue'
import reserve from './component/reserve.vue'
import cancel from './component/cancel.vue'
import ma from './component/ManageStudents.vue'
import credit from './component/credit.vue'


// 3. 创建路由对象
var router = new VueRouter({
    routes: [
        { path: '/', components: { 'left': leftBox, 'main': mainBox } },
        { path: '/query', components: { 'left': leftBox, 'main': ma } },
        { path: '/renew', components: { 'left': leftBox, 'main': renew } },
        { path: '/cancel', components: { 'left': leftBox, 'main': cancel } },
        { path: '/reserve', components: { 'left': leftBox, 'main': reserve } },
        { path: '/credit', components: { 'left': leftBox, 'main': credit } }
    ]
})

// 把路由对象暴露出去
export default router