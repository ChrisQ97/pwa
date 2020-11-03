<template>
<b-container class="bv-example-row">
  <b-row>
    <b-col>
        <div class="container">
         
            <form>
                <div class="input-group">
                <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                <input id="Nombre" type="text" class="form-control" name="Nombre" placeholder="Nombre">
                </div>
                <div class="input-group">
                <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                <input id="Correo" type="text" class="form-control" name="Correo" placeholder="Correo">
                </div>
                <div class="input-group">
                <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                <input id="Telefono" type="text" class="form-control" name="Telefono" placeholder="Telefono">
                </div>
                <div>
                <textarea placeholder="Dejanos un comentario!" class="pb-cmnt-textarea"></textarea>
                </div>
                <br>
                <div>
                <button class="btn btn-primary pull-right" type="button">Enviar informacion</button>
                </div>
            </form>
            <br>

            </div>




    </b-col>
    <b-col>
        <h1>Envianos un comentario y nos comunicaremos contigo lo mas pronto posible</h1>
        <p> Cupcake ipsum dolor sit amet. Halvah carrot cake cake. Pie muffin tart liquorice.</p>
        <p>Chocolate bar caramels dragée dessert cookie soufflé. Croissant caramels macaroon muffin jelly lollipop cookie sugar plum icing. Toffee marshmallow biscuit candy canes apple pie apple pie tart. Tiramisu candy canes tootsie roll oat cake jujubes muffin ice cream.</p>
    </b-col>

  </b-row>
</b-container>
</template>
<script>
export default {
    name: "Second"
}
</script>
<style scoped>
.bv-example-row{
    margin-top: 70px;
}
p{
    margin-top: 30px;
    text-align: left;
}
h1{
    text-align: left;
}

</style>