container_tabs_btns = document.querySelector(".container-tabs-btn")
container_tabs = document.querySelector(".container-tabs");

container_tabs_btns.addEventListener("click", event => {
    console.log(event.target);
    tab_under_focus = container_tabs_btns.querySelector(".tab-under-view");
    tab_under_focus.classList.remove("tab-under-view");

    tab_under_focus_id = tab_under_focus.getAttribute("id");
    focused_container = document.querySelector("div[name="+tab_under_focus_id+"]");
    focused_container.classList.remove('visible')

    event.target.classList.add("tab-under-view");
    tab_not_under_focus_id = event.target.getAttribute("id");
    unfocused_container = document.querySelector("div[name="+tab_not_under_focus_id+"]");
    unfocused_container.classList.add('visible')
})