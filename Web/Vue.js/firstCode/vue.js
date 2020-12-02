new Vue({
  el: '#vue-app',
  data:{
    name: 'Kayken7',
    job: 'freelancer',
    number: 999
  },
  methods:{
    greet: function(){
      return 'Hello Vue.js!'
    },
    parameter: function(name) {
      return 'Hello ' + name
    },
    parameter2: function() {
      return 'Hello ' + this.job + '!'
    }
  }
});
