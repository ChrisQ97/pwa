<template>
    <div class="card" style="width: 18rem;">
        <img v-bind:src="this.place.img_source" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title">{{place.title}}</h5>
            <p class="card-text">{{place.description}}</p>
            <p class="card-text">Puntuación: {{place.score}}</p>
            <a class="btn btn-warning" v-on:click="addScore()"><i class="far fa-thumbs-up"></i></a>
        </div>
    </div>
</template>

<script>
export default {
    name: "Tarjet",
    data(){
        return{
            rated: false,
        }
    },
    methods: {
        addScore(){
            if(!this.rated){
                this.place.score++;
            }
            this.rated =true;
        }
    },
    props: {
        place:{
            type: [Object],
            required: true, 
            default: {
                score: 0,
                title: "Panajachel",
                description: "Like!",
                img_source: 'https://thumbnails.trvl-media.com/V3rp_WgwXvGnOKBVM9IqvPEf-yg=/360x224/smart/filters:no_upscale():quality(80)/a.travel-assets.com/findyours-php/viewfinder/images/res70/77000/77422-Panajachel.jpg'
            }
        }
    }
}
</script>

<style scoped>
    .card{
        display: inline-block;
        margin: 15px;
    }
    .btn {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: blue;
    
    }
    img{
        max-width: 100%;
    }
    
</style>