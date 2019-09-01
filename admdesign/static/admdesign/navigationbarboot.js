$(document).ready(function () {

  $('.first-button').on('click', function () {

    $('.animated-icon1').toggleClass('open');
  });
  $('.second-button').on('click', function () {

    $('.animated-icon2').toggleClass('open');
  });
  $('.third-button').on('click', function () {

    $('.animated-icon3').toggleClass('open');
  });

});


$(function () {

var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: window.location.protocol+'//'+'localhost'+':'+window.location.port+btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      data:{},
      beforeSend: function () {
        $("#modal-project .modal-content").html("");
        $("#modal-project").modal("show");
      },
      success: function (data) {
        $($("#modal-project > .modal-dialog > .modal-content")[0]).html(data.html_form);
      }
    });
  };

var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: window.location.protocol+'//'+'localhost'+':'+window.location.port+form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#project-table tbody").html(data.html_project_list);
          $("#modal-project").modal("hide");
        }
        else {
          $($("#modal-project > .modal-dialog > .modal-content")[0]).html(data.html_form);
        }
      },
      error: function(jqXHR, exception) {
        alert("Error!");
      }
    });
    return false;
  };


var loadAdminHome = function () {
    var dataid = $("#prj-selector option:selected").attr('data-id');
    $.ajax({
      url: window.location.protocol+'//'+'localhost'+':'+window.location.port+'/view_prj_designs/'+dataid+'/',
      data: {},
      type: 'get',
      dataType: 'json',
      success: function (data) {
          $("#project-table2 tbody").html(data.html_project_list);
      },
      error: function(jqXHR, exception) {
        alert('Error!')
      }
    });
  };


var previewDesign = function () {
    var imgUrl = $(this).attr('data-url');
    var imgUrl = imgUrl.replace(/\//g, "*");
    $.ajax({
      url: window.location.protocol+'//'+'localhost'+':'+window.location.port+'/preview_design/'+imgUrl+'/',
      data: {},
      type: 'get',
      dataType: 'json',
      success: function (data) {
          $($("#modal-design > .modal-dialog > .modal-content")[0]).html(data.html_design_img);
          $("#modal-design").modal("show");
      },
      error: function(jqXHR, exception) {
        alert('Error!');
      }
    });
  };


$(".js-create-project").click(loadForm);
$("#modal-project").on("submit", ".js-project-create-form", saveForm);

$("#project-table").on("click", ".js-update-project", loadForm);
$("#modal-project").on("submit", ".js-project-update-form", saveForm);

$("#project-table").on("click", ".js-delete-project", loadForm);
$("#modal-project").on("submit", ".js-project-delete-form", saveForm);

$(".js-project-load-data").click(loadAdminHome);
$("#project-table2").on("click", ".js-preview-design", previewDesign);

});