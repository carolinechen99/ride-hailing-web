/* global bootstrap: false */

(() => {
  'use strict'

  // Tooltip and popover demos
  document.querySelectorAll('.tooltip-demo')
    .forEach(tooltip => {
      new bootstrap.Tooltip(tooltip, {
        selector: '[data-bs-toggle="tooltip"]'
      })
    })

  document.querySelectorAll('[data-bs-toggle="popover"]')
    .forEach(popover => {
      new bootstrap.Popover(popover)
    })

  document.querySelectorAll('.toast')
    .forEach(toastNode => {
      const toast = new bootstrap.Toast(toastNode, {
        autohide: false
      })

      toast.show()
    })



  // function setActiveItem() {
  //   const { hash } = window.location

  //   if (hash === '') {
  //     return
  //   }

  //   const link = document.querySelector(`.bd-aside a[href="${hash}"]`)

  //   if (!link) {
  //     return
  //   }

  //   const active = document.querySelector('.bd-aside .active')
  //   const parent = link.parentNode.parentNode.previousElementSibling

  //   link.classList.add('active')

  //   if (parent.classList.contains('collapsed')) {
  //     parent.click()
  //   }

  //   if (!active) {
  //     return
  //   }

  //   const expanded = active.parentNode.parentNode.previousElementSibling

  //   active.classList.remove('active')

  //   if (expanded && parent !== expanded) {
  //     expanded.click()
  //   }
  // }

  setActiveItem()
  window.addEventListener('hashchange', setActiveItem)

  // function fillCheckbox() {
  //   let checkbox = document.getElementById('flexSwitchCheckChecked');
  //   console.log(ride.allow_sharing);
  //   if (ride.allow_sharing === true) {
  //     checkbox.checked = true;
  //   }
  //   else {
  //     checkbox.checked = false;
  //   }
  // }
  // fillCheckbox()
  // window.addEventListener('hashchange', fillCheckbox)
})()


