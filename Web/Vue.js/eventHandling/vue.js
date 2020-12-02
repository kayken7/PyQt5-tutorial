app = new Vue({
  el: '#vue-app',
  data:{
    count: 30
  },
  methods:{
    double: function(){
      this.count *= 2;
    }
  }
});
app2 = new Vue({
  el: '#canvas',
  data:{
    count: 30,
    x: 0,
    y: 0
  },
  methods:{
    updatePos: function(event){
      this.x = event.offsetX;
      this.y = event.offsetY;
    }
  }
});
