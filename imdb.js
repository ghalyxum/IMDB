



var ld_pointer=document.querySelector('script[type="application/ld+json"]').innerText;

var jsonld = JSON.parse(ld_pointer);


t_type = jsonld["@type"];
t_name = jsonld["name"];
t_url = jsonld["url"];
t_poster = jsonld["image"];
t_description = jsonld["description"];
t_genre = jsonld["genre"]; // list
t_datePublished = jsonld["datePublished"];

t_trailer_embedUrl = jsonld["trailer"]["embedUrl"];
t_ratingValue = jsonld["aggregateRating"]["ratingValue"];
t_actor = jsonld["actor"]; // list
t_director = jsonld["director"]; // list

imdb_id = t_url.split("/")[(t_url.split("/")).length-2];

// parsing t_datePublished
t_year = new Date(t_datePublished).getFullYear();



