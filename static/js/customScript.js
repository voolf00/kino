$(function () {
    $("#newArticle").dialog({
        autoOpen: false

    });

    $("#openFormArticle").click(function () {
        $("#newArticle").dialog("open");
        return false;
    });
});
