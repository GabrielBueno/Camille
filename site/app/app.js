const app = new Vue({
    el: "#app",
    data: { message: "Hello, Vue!" } 
});

const app2 = new Vue({
    el: "#app2",
    data: { message: "You loaded this page on " + new Date().toLocaleString() }
});

const app3 = new Vue({
    el: "#app3",
    data: { 
        seen: true,
        message: "You didn't see me" 
    }
});