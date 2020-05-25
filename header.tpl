<html>
<head>
    <style>
        body {
            margin: 0;
        }

        .content {
            max-width: 1200px;
            margin: 0 auto;
        }
        .listitem img {
            display: block;
            max-width: 100%;
        }

        .header {
            overflow: hidden;
            background-color: #F0F0F0;
            padding: 10px;
            margin-bottom: 1em;
        }

        .header a {
            float: right;
        }

        @media screen and (min-width: 600px) {
            .list {
                display: flex;
                flex-wrap: wrap;
                flex-direction: row;
            }
            .listitem {
                width: 33%;
            }
        }
    </style>
</head>
<body>
<div class="header">
    <a class="nav-link" href="/add">Přidat obrázek</a>
</div>
<div class="content">