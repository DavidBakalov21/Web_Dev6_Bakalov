info = {
  "info": [
    {
      "Path": "/",
      "method": "GET",
      "description": "displays info about all endpoints",
    },
      {
          "Path": "hw6/entity",
          "method": "GET",
          "description": "displays the list of all messages",
      },
      {
          "Path": "hw6/entity/:id/",
          "method": "GET",
          "description": "display message with certain id",
      },
      {
          "Path": "hw6/Postentity/",
          "method": "POST",
          "description": "add new message with postman, input example ({'Userid': 'hhhh','message': 'GhjnbvET','time': '2024-0000002-02T06:54:31.488+00:00'} (!!! replace '' to double quotation marks !!!!)) ",
      },
      {
          "Path": "hw6/DeleteEntity/:id",
          "method": "DELETE",
          "description": "delete entity via postman,  example (http://some domain/hw6/DeleteEntity/23435fgfdf)",
      },
      {
          "Path": "hw6/image",
          "method": "GET",
          "description": "just show you a page with static image and <a> to go to the main menu",
      },
      #hw7
        {
          "Path": "hw6/set_cookie",
          "method": "GET",
          "description": "sets cookie example (http://127.0.0.1:8000/hw6/set_cookie?cookie=favorite&val=value)",
        },
        {
          "Path": "hw6/get_cookie/<str:title>/",
          "method": "GET",
          "description": "gets cookie example (http://127.0.0.1:8000/hw6/get_cookie/favorite/)",
        },
        {
          "Path": "hw6/set_header",
          "method": "GET",
          "description": "sets header example (http://127.0.0.1:8000/hw6/set_header?header=favorite&value=value)",
         },
        {
          "Path": "hw6/get_header/<str:header_name>/",
          "method": "GET",
          "description": "gets header example (http://127.0.0.1:8000/hw6/get_header/header/) !!! header must be set in Postman headers like header - val !!!",
        },
  ]
}