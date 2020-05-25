% include('header.tpl', title='Seznam')
<div class="add">
<form method="post" enctype="multipart/form-data">
    <div class="form-group">
        <label for="txtitle">Titulek obrázku</label>
        <input type="text" class="form-control" name="txtitle" id="txtitle" aria-describedby="emailHelp" placeholder="Titulek obrázku">
    </div>
    <div class="form-group">
        <label for="upload">Obrázek</label>
        <input type="file" class="form-control-file" id="upload" name="upload">
    </div>
    <button type="submit" class="btn btn-primary">Přidat</button>
</form>
</div>
% include('footer.tpl')