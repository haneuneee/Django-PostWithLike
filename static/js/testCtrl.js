

var myApp = angular.module('myApp', []);

myApp.controller('myCtrl', ['$scope','$http', function ($scope, $http) {
    $http.defaults.headers.post['Content-Type'] = 'application/json';
    $http.defaults.headers.post['X-CSRFToken'] = window.csrf_token;
  $scope.author = {
  	name: 'hyunseob',
    age: 27
  };
  $scope.init = function(value){
      console.log('init');
      console.log(value);
      $scope.comments = value;
      console.log($scope.comments);
  }

  $scope.hide = function(c){
  }

  $scope.submit = function(post_url){
      console.log('submit');
      console.log($scope.formdata.content);
      console.log($scope.comments);
      $http({
          method: 'post',
          url: post_url,
          data: {
              content: $scope.formdata.content
          }
      }).then(function(success, err){
          if(success){
                $scope.comments.push({content: $scope.formdata.content});
                $scope.formdata.content = "";
          } else{
              alert(err);
          }
      });

  }

}]);

myApp.config(function($interpolateProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
        });
myApp.directive('myDirective', function() {

  return {
    restrict: 'E',
    scope: {
    	comment: "=",
    },
    template: '<div>댓글내용 : {{ comment.content }} <button ng-click="btn()">{{ show_comment }}댓글보기({{ comment.replies.length }})</button><reply ng-class="{hide:hide_comment}" replies="comment.replies"></reply></div>',
    link: function(scope) {
        scope.hide_comment = false
        scope.btn = function(){
            scope.hide_comment = !scope.hide_comment;
            console.log('dd');
        }
    }
  }
});


myApp.directive('reply', function () {

   return{
       restrict: 'E',
       require:'^outer',
       scope:{
           replies: "="
       },
       template: '<div ng-repeat="reply in replies" ng-click="changeState()"> {{ reply.content }}</div>'
   }
});