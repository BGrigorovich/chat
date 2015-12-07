var app = angular.module('chatApp', ['angular.filter'], function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}, ['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
}]);

app.controller('messagesController', function ($scope, $http, $interval) {
    $http.get('/messages')
        .then(function (response) {
            //$scope.messages = JSON.parse(response.data);
            $scope.messages = response.data;
        });

    $scope.processForm = function () {
        $http({
            method: 'POST',
            url: '',
            data: {'message': $scope.message},
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
    }
});