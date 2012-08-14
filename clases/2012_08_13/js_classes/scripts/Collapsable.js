Collapsable = Class.extend({
	
	init: function(args){
		this.$domObject = $(args.domObject);
		this.initActions();
		this.opened = true;
	},
	
	initActions: function(){
		this.$content = this.$domObject.find('.content');
		var container = this;
		this.$domObject.find('button').click(function($event){
			container.expand_collapse();
		});
	},
	
	expand_collapse: function(direction){
		direction = (direction == undefined) ? !this.opened : direction;
		this.show(direction);
		this.opened = direction;
	},
	
	show : function(direction){
		if (direction){
			this.$content.show();
		}else{
			this.$content.hide();
		}
	}
	
});