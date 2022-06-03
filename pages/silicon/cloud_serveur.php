<?php
if (($open = fopen($_SERVER['DOCUMENT_ROOT'] . '/csv/cloud_serveur_silicon.csv', "r")) !== FALSE) {
    while (($data = fgetcsv($open, 1000, ";")) !== FALSE) {
        $array[] = $data;
    }
    fclose($open);
}
?>

<!doctype html>
<html lang="fr">
<head>
    <?php $title = "Outil de veille technologique";
    include($_SERVER['DOCUMENT_ROOT'] . '/php/header.php'); ?>
</head>
<body>
<div id="filterbanner"></div> <!--Filtre-->
<div id="banner"></div>
<?php include($_SERVER['DOCUMENT_ROOT'] . '/php/navbar.php'); ?>
<main class="container">

    <div class="card border-primary text-grey text-center p-3 mb-5 rounded shadow-sm">
        <!--Carte présentant la veille technologique-->
        <div class="card-body">
            <h5 class="card-title">Serveurs</h5>
            <h6 class="card-title">Silicon</h6>
            <p class="card-text">.........................................</p>
            <p class="card-text">
                <?php
                echo "Mis à jour le  ";
                if(is_readable($_SERVER['DOCUMENT_ROOT'] . '/csv/cloud_serveur_silicon.csv')){
                    $message = date("d/m/Y à H:i:s.", filemtime($_SERVER['DOCUMENT_ROOT'] . '/csv/cloud_serveur_silicon.csv'));
                }
                else{
                    $message = " // Fichier inexistant //";
                }
                echo $message;
                ?>
            </p>
        </div>
    </div>

    <?php
    $i = 0;
    $a = 0;
    $nombre = count($array);
    foreach ($array as $title) {
        if ($i == 0) {
            echo '<div class="card-deck">';
        }
        echo '<div class="card text-grey shadow p-3 mb-5 border-primary rounded">
            <div class="card-header text-center">
            <img class="card-img-top img-documentation" src="' . $title['2'] . '" alt="Image article">
            </div>
            <div class="card-body">
            <h5 class="card-title">' . $title['0'] . '</h5>
            <!--<p class="card-text">Publié ' . $title['3'] . '</p>-->
            </div>
            <div class="card-footer">
            <a href="' . $title['1'] . '" class="btn btn-primary" target="_blank">Lien vers l\'article</a>
            </div>
            </div>';
        if ($i !== 3) {
            $i++;
        }
        if ($i == 3) {
            echo '</div>';
            $i = 0;
        }
        $a++;
        if ($a == $nombre) {
            echo '</div>';
        }
    }
    ?>

</main>
</body>
<?php include($_SERVER['DOCUMENT_ROOT'] . '/php/footer_without_class.php'); ?>
</html>