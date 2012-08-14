SlidingCollapsable = Collapsable.extend({
	
	show : function(direction){
		// this._super(direction);
		if (direction){
			this.$content.slideDown();
		}else{
			this.$content.slideUp();
		}
	}
	
});