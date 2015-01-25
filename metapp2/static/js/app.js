(function(angular, _) {
  var METAPP = angular.module('metApp', ['lumx',
    'ui.router'
  ]);
  METAPP
    .config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('[[').endSymbol(']]');
    })
    .config(function($stateProvider, $urlRouterProvider) {

      $urlRouterProvider.otherwise('/home');

      $stateProvider

      // HOME STATES AND NESTED VIEWS ========================================
      .state('home', {
        url: '/home',
        templateUrl: '/static/partials/home.html'
      })

	      .state('home.list', {
	        url: '/list',
	        templateUrl: '/static/partials/home-list.html',
	        controller: function($scope) {
	        	$scope.dogs = [1,2,3,4];
	        }
	      })

      // ABOUT PAGE AND MULTIPLE NAMED VIEWS =================================
      .state('about', {
        url: '/about',
        templateUrl: '/static/partials/about.html'       
      });

    })
    .config(['$locationProvider',
      function($locationProvider) {
        $locationProvider.html5Mode(true).hashPrefix('!');
      }
    ]);
})(angular, _);
