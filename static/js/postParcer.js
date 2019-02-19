var article = post;

// ARTICLE
var imgUrl = "url('https://res.cloudinary.com/syplemstudio/" + article.image + "')";
var imgEl = document.getElementById('article-image');
imgEl.style.backgroundImage = imgUrl;

var titleEl = document.getElementById('article-title');
titleEl.innerHTML = article.title;

var timeEl = document.getElementById('article-timestamp');
timeEl.innerHTML = parseDate(article.created);

var contentEl = document.getElementById('article-content');
contentEl.innerHTML = article.content;

// COMMENTS
var commCounter = document.getElementById('comm-counter');
var commNum = article.comments.length;
commCounter.innerHTML = getCommNumLabel(commNum);

var comments = article.comments;
var commSection = document.getElementById('comments');
for (var i = 0; i < comments.length; i++) {
  var comment = parseComment(comments[i]);
  commSection.appendChild(comment);
}

// UTILS
function parseDate(stamp) {
  dateObject = new Date(Date.parse(stamp));
  dateReadable = dateObject.toLocaleString();
  return dateReadable;
}

function getCommNumLabel(n) {
  var label = '';

  if(n == 0) {
    label = "Еще ни одного комментария";
  } else if(n % 10 == 1) {
    label = n + " комментарий";
  } else if(n % 10 > 1 && n % 10 < 5) {
    label = n + " комментария";
  } else {
    label = n + " комментариев";
  }

  return label;
}

function createElementWithTextClass(el, text, className) {
  var element = document.createElement(el);
  var textNode = document.createTextNode(text);
  element.appendChild(textNode);
  if(className) element.classList.add(className);

  return element;
}

function parseComment(commObj) {
  var comm = document.createElement('div');
  comm.classList.add("comment");

  var commHeader = createHeader(commObj.author, commObj.created)
  var commBody = createBody(commObj.content);
  
  comm.appendChild(commHeader);
  comm.appendChild(commBody);

  return comm;
}

function createHeader(author, created) {
  var header = document.createElement('div');
  header.classList.add("comment-header");
  var commAuthor = createElementWithTextClass('span', author, 'comment-author');
  header.appendChild(commAuthor);
  var commDate = createElementWithTextClass(
    'span',
    parseDate(created),
    'comment-timestamp'
  );
  header.appendChild(commDate);

  return header;
}

function createBody(content) {
  var body = document.createElement('div');
  body.classList.add("comment-body");
  var commText = createElementWithTextClass('p', content);
  body.appendChild(commText);

  return body;
}