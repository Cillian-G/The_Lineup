# Surf Social

![project screenshot](/documenttion/testing/chrome_laptop_test.png)

Surf Social is a website built to allow members of a fictional “Belmullet Surf Club” to coordinate their surfing sessions without cluttering up social media feeds. Users are given a 

## User Stories

 - As an admin I can edit the "notes" section on the local beaches listing so that surf club users can be made aware of relevant information when they are organizing their sessions.
 - As an admin I can create accounts for users so that access can be limited to club users.
 - As an admin I can add notes to meet-up posts so that I can add further relevant 
 - As a user I can view information about local beaches so that I can stay aware of hazards and other changes as they arise.
 - As a user I can login with account details provided by the surf club so that I can view and interact with meetup posts.
 - As a user I can add/remove my sessions from meetup posts so that meetup posts can list accurate information about who else will be surfing on a given beach at a given time.
information regarding things like club events, beach hazards or weather warnings.
 - As a user I can view meet-up posts so that I can organise to surf at the same time as others.

## UX 

This design was intended to be minimalist, in part to make future additions easy to implement for the surf clubs webmaster, but also because the purpose of the site itself is very simple. 

### Colour Scheme 

The default bootstrap colours were used for several reasons. Black was naturally the best choice for readable text on a white background, the default blues and greys were used for buttons and links because they were already appropriate for the theme of the site, and matched nickel with the beach pictures. 

### Typography 

Google Font ‘Fresca was chosen for its “laid-back”, and friendly look, which felt appropriate for a surf club.

### Wireframes 

![deployment instructional screenshot](/documenttion/wireframes/wireframe_1.png)
![deployment instructional screenshot](/documenttion/wireframes/wireframe_2.png)
![deployment instructional screenshot](/documenttion/wireframes/wireframe_3.png)
![deployment instructional screenshot](/documenttion/wireframes/wireframe_4.png)
![deployment instructional screenshot](/documenttion/wireframes/database_diagram.png)

Pictured above is a screenshot "database" diagram that was put together to help conceptualize the models required by the project. 

## Features

### Existing Features

Allows easy addition of more beaches and users by the webmaster.
Beach info is visible to non-signed in users but session information is not, to protect the privacy of club members
Sessions belonging to the user can be edited and deleted, while non-user sessions can only be edited by the user that owns them.

### Features Left to Implement

Adding a paid API that shows tide charts for the Belmullet area.

## Technologies Used

Pages were written and styled with HTML, and bootstrap, 
Python, Django
Some minor javascript was used, to set a minimum date for the calendar form, and to make link-buttons work correctly. 
Github and Gitpod
Heroku for deployment
Marvel for building wireframes, google sheets for making database diagrams

## Testing

### Code Validation

### Browser Compatibility

![chrome / laptop screenshot](/documenttion/testing/chrome_laptop_test.png)
![edge / tablet screenshot](/documenttion/testing/edge_tablet_test.png)
![firefox / mobile screenshot](/documenttion/testing/firefox_mobile_test.png)

### Responsiveness

See images in browser compatibility section above. 

## Deployment

Deployment was on heroku, via github. To copy this deployment, one would need to set up accounts on cloudinary, heroku. Once they had made an app for this project on their heroku account, and after installing heroku postgres for the database, they would need to set up their heroku app config vars wth the headings ilustrated in the image below. The Cloudinary url will be provided by their cloudinary account, and set their own secret key.

![deployment instructional screenshot](/documenttion/heroku_deployment.png)

## Credits

### Media
- Glosh Photo(https://scontent.fdub5-1.fna.fbcdn.net/v/t39.30808-6/284097919_2209510839213150_2414960184895101163_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=108&ccb=1-7&_nc_sid=110474&efg=eyJpIjoidCJ9&_nc_ohc=jRc2x2HvNA8AX_GAh5G&_nc_ht=scontent.fdub5-1.fna&oh=00_AT-Nuyk27eT5Y2uxTRgRZjl9sCHtv7vX2EJvKKu86Fu8Mg&oe=62B17A33)
- Cross Photo( https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/a6/cc/d6/photo0jpg.jpg?w=1200&h=-1&s=1)
- Beal Dara Photo(http://visitbelmullet.ie/wp-content/uploads/erris-beo-explore-Belderra-Beach-photo-by-Shannon-Cronin-01.jpg)
- Elly Photo(https://www.northmayo.ie/wp-content/uploads/2020/07/Elly-Beach-Belmullet-Co_Web-Size_2_FI.jpg)
-  Fod Dubh Photo(https://www.activeme.ie/wp-content/uploads/2015/09/Falmore-beach-photo-by-Evita-Coyle-01_Mayo-wild-atlantic-way-ireland.jpg) 

### Acknowledgements
Tim Nelson for his many helpful design suggestions, and the many resources he has linked to me 



