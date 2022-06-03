<?php
if(($open = fopen($_SERVER['DOCUMENT_ROOT'].'/csv/export.csv',"r")) !== FALSE){
    while(($data = fgetcsv($open, 1000, ";")) !== FALSE){
        $array[] = $data;
    }
    fclose($open);
}
?>

<!doctype html>
<html lang="fr">
<head>
    <?php $title = "Outil de veille technologique";
    include($_SERVER['DOCUMENT_ROOT'].'/php/header.php'); ?>
</head>
<body>
    <div id="filterbanner"></div> <!--Filtre-->
    <div id="banner"></div>
    <?php include($_SERVER['DOCUMENT_ROOT'].'/php/navbar.php'); ?>
    <main class="container">
        <div class="starter-template text-center py-5 px-3"> <!--Paragraphe de présentation-->
            <h1>Bienvenue sur mon outil de veille technologique !</h1><br>
            <p class="lead">Les entreprises comment à avoir la volonté de réduire leur impact environnemental et
                énergétique au niveau informatique, en passant notamment par la réduction du nombre d'équipements
                hébergés en datacenter. Pour cela, une majorité des entreprises se tournent vers l’hébergement sur
                des plateformes cloud, ou vers la virtualisation. VMWare, un des leaders du secteur, ne cesse de
                développer de nouveaux outils et technologies pour rendre, toujours plus viable, ce procédé.</p>
        </div>
    </main>
</body>
<?php include($_SERVER['DOCUMENT_ROOT'].'/php/footer_with_class.php');?>
</html>