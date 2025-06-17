<template>
	<div class="container-fluid">

		<div v-show="showPagination()">

			<nav aria-label="Page navigation pagination">
				<ul class="pagination">
					
					<li class="page-item"><a class="page-link" :href="page_previous_link">Previous</a></li>
					
					<li class="page-item" v-for="page_item in page_items" :key="page_item.id">
						<a class="page-link" :href="page_item.link">{{ page_item.id }}</a>
					</li>

					<li class="page-item"><a class="page-link" :href="page_next_link">Next </a></li>
				</ul>
			</nav>

			<br/><br/>
			<br/><br/>

		</div>

	</div>
	
</template>

<script>
	export default {
		name: 'Pagination',
		props: ['page_data'],
		data() {
			return {
				'page_previous_link': '',
				'page_next_link': '',

				'page_items': [],
				'num_pages': this.page_data.num_pages,
			}
		},
		methods: {
			//Show Pagination When Have to Be Shown
			showPagination() {
				if (this.page_items.length >= 1) {
					return true;
				}else {
					return false;
				}
			},

			//Get Current Page
			getCurrentPage() {
				var page = this.$route.query.page;

				if (page == undefined) {
					page = 1;
				}

				return page;
			},

			//Populate Page Items
			populatePageItems() {
				for (var i = 0; i < parseInt(this.page_data.num_pages); i++) {
					var id_p = i + 1;
					this.page_items.push({
						'id': id_p,
						'link': '?page=' + id_p
					})
				}

				//Populate Previous and Next Page
				this.page_previous_link = "?page=" + this.getPreviousPageId();
				this.page_next_link = "?page=" + this.getNextPageId();
			},

			//Get Previous Page Id
			getPreviousPageId() {
				if ((parseInt(this.getCurrentPage()) - 1) >= 0) {
					return 1;
				}else {
					return parseInt(this.getCurrentPage()) - 1;
				}
			},

			//Get Next Page Id
			getNextPageId() {
				if ((parseInt(this.getCurrentPage()) + 2) >= parseInt(this.num_pages) ) {
					return parseInt(this.getCurrentPage());
				}else {
					return parseInt(this.getCurrentPage()) + 1;
				}
			}
		},

		watch: {
			page_data: {
      			handler() {
					//Populate Page Items
					this.populatePageItems()
				}
			}
		},

		metaInfo () {
			return {
				'page_data': this.page_data
			}
		},

	}
</script>


<style scoped>
.pagination {
	float: right; 
	margin-right: 25px;
}

</style>