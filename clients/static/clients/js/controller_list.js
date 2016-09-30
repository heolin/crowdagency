crowdhub.controller('clientsCtrl', function($scope, API) {
    $scope.getClientsList = function(){
        API.ClientsList.list({}, function(data){
            $scope.ClientsList = data
        })
    }
    $scope.getClientsList();

    var TASK1_ID = 1;
    var CLICK_ITEM1_ID = "57eed2f894b68f1f06b7ccd6";
    API.TaskItemsStats.detail({taskId:TASK1_ID, itemId:CLICK_ITEM1_ID}, function (data) {
        $scope.task1 = data;
    })

    var TASK2_ID = 2;
    var CLICK_ITEM2_ID = "57eed2ea94b68f1f06b7ccd5";
    API.TaskItemsStats.detail({taskId:TASK2_ID, itemId:CLICK_ITEM2_ID}, function (data) {
        $scope.task2 = data;
    })
});
