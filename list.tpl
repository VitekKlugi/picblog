% include('header.tpl', title='Seznam')
<div class="list">
%for img in imgs:
  <div class="listitem">
    <div class="title">{{img['title']}}</div>
    <img src="{{img['url']}}" />
  </div>
%end
</div>
% include('footer.tpl')