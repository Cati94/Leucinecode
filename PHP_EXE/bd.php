<?php
	$servidor = "localhost";
	$baseDados = "pweb06_site";
	$userBaseDados = "pweb06_site_user";
	$passwordBaseDados = "teste123";
	
	//Estabelecer ligação e guardar a mesma
	$ligacaoBD = mysqli_connect($servidor, $userBaseDados, $passwordBaseDados, $baseDados) or die("Erro de acesso à Base de Dados.");
?>