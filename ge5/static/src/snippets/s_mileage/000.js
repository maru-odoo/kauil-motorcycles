odoo.define('registry.s_mileage', function (require) {
    const PublicWidget = require('web.public.widget')
    const rpc = require('web.rpc')

    const MileageWidget = PublicWidget.Widget.extend({
        selector: '.s_mileage',
        disabledInEditableMode: false,
        start: function() {
            var self = this
            rpc.query({
                route: '/mileage',
                params: {},
            }).then(function (result) {
                console.log(result)
                self.$("#mileage").text(result)
            })
        },
    })

    PublicWidget.registry.mileage = MileageWidget

    return MileageWidget;
});
