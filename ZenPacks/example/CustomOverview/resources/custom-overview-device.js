(function(){

Ext.onReady(function() {

    // Add information to the device overview page.
    var PANEL_ID = 'deviceoverviewpanel_systemsummary';
    Ext.ComponentMgr.onAvailable(PANEL_ID, function(){
        var panel = Ext.getCmp(PANEL_ID);

        panel.addListener("afterrender", function(){
            panel.insert(0, {
                name: 'contact',
                xtype: 'textfield',
                fieldLabel: _t('Technical Contact')
            });
        });
    });
});

})();
