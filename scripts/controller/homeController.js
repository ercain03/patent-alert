(function (module) {
  var homeController = {};

  homeController.index = function() {
    $('#about').css('display', 'none');
    $('#results').css('display', 'none');
    $('#discription').css('display', 'none');
    $('#home').css('display', 'block');
    $('.form').fadeIn();
    drugView.handleSearchInput();
  };


  module.homeController = homeController;
})(window);
