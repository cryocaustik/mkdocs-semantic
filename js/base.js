$(document).ready(()=>{
    hljs.initHighlightingOnLoad();
    $('.ui.dropdown').dropdown();
    $('#sidebar-btn').click(()=>{
        $('.ui.sidebar')
            .sidebar('setting', 'transition', 'overlay')
            .sidebar('toggle')
            ;
    });
    $('#search-btn').click(()=>{
        $('#mkdocs_search_modal')
            .modal({centered: false})
            .modal('show');
    });
})

