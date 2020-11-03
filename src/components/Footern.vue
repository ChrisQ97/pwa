<template>
<div>
  <b-row>
    <b-col> <h3>Christian Quijivix</h3></b-col>
    <b-col><a href="http://facebook.com"> <h3>Facebook</h3></a></b-col>
    <b-col><a href="http://instagram.com"> <h3>Instagram</h3> </a> </b-col>
  </b-row>
</div>
</template>
<script>
export default {
    name: 'Footern'
}
</script>
<style scoped>
div {
  background-color: blue;
  height: 200px;

}
h3{
  font-size: 20px;
  color: white;
  margin-top: 20px;
}
a {
  font-size: 20px;
  color: white;
  height: 300px;
  margin-top: 100px;
}

</style>