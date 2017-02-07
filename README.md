# project1-jocruz
##1. THEME
  The theme is pretty straight forward to begin with. It is all about pups,pupps,  
  puppers, and doggos. It pairs images of these pets with words about these awesome creatures.  
##2. CURATION:
  1. Twitter:
    *i. The twitter api search query was composed of a query that limited certain parameters..
    *ii. I decided to search for the keywords 'pups' and 'puppers' while exlcuding replies, retweets,  
        images, and links. This was as to not have to deal with certain complications that could arise because  
        of those items. The actual query was "puppers OR pups -filter:retweets AND -filter:replies AND -filter:links AND -filter:twimg".

  2. Getty:
    *i. I decided to be pretty straigt forward with this api call and search for images with a large size.  
        I also decided to keep the phrase simple and go with the keyword 'puppies'. 
        <a href = "https://api.gettyimages.com:443/v3/search/fields=comp&license_models=royaltyfree&minimum_size=large&sort_order=best_match&phrase=puppies"> link</a>

##KNOWN PROBLEMS:
  1.Unicode:
    *i.Some tweets come through with unicode for emojis and I was unable to make them render. 
  2.CSS:
    *i.Given more time I could have made the application more responsive to window resizing. As  
      is right now there could be some improvements to formatting.


##IMROVEMENTS:
  1.THEME:
  *i.My main thought was to make the application be themed around "pups and pints", where the curations  
     revolves around doggs and beer, either matching images of pups with tweets about beer or vice versa.
  2.APPEARANCE:
    *i. I would want to make a better layout for it and maybe even give some control to the user (such as search parameters).





