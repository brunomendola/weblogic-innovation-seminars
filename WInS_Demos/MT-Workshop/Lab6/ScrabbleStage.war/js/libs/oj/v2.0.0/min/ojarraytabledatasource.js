/**
 * Copyright (c) 2014, 2016, Oracle and/or its affiliates.
 * The Universal Permissive License (UPL), Version 1.0
 */
"use strict";
/*
 Copyright 2013 jQuery Foundation and other contributors
 Released under the MIT license.
 http://jquery.org/license
*/
define(["ojs/ojcore","jquery","ojs/ojdatasource-common"],function(b,f){b.Da=function(a,d){this.data={};if(!(a instanceof Array)&&"function"!=typeof a&&"function"!=typeof a.gqa)throw Error(b.T.ec._ERR_DATA_INVALID_TYPE_SUMMARY+"\n"+b.T.ec._ERR_DATA_INVALID_TYPE_DETAIL);null!=d&&null!=d.idAttribute||b.r.info(b.Da.ec._INFO_ARRAY_TABLE_DATASOURCE_IDATTR);b.Da.q.constructor.call(this,a,d);this.hd=[];this.qa={};if(null!=a&&void 0!==a&&(this.gK=null,null!=d&&null!=d.idAttribute&&(this.gK=d.idAttribute),
this.i=a instanceof Array?a:a(),this.ke=this.i.length,!(a instanceof Array))){var c=this;a.subscribe(function(a){if(c.eY()){var b,d=[],f=[];for(b=0;b<a.length;b++)"deleted"===a[b].status&&d.push(a[b].value);c.remove(d,null);d=[];f=[];for(b=0;b<a.length;b++)"added"===a[b].status&&(d.push(a[b].value),f.push(a[b].index));c.add(d,{at:f})}},null,"arrayChange")}if(null!=d&&("enabled"==d.startFetch||null==d.startFetch)||null==d)this.Vx=!0};o_("ArrayTableDataSource",b.Da,b);b.b.ga(b.Da,b.T,"oj.ArrayTableDataSource");
b.Da.prototype.Init=function(){b.Da.q.Init.call(this)};b.b.g("ArrayTableDataSource.prototype.Init",{Init:b.Da.prototype.Init});b.Da.prototype.add=function(a,b){b=b||{};this.Sp();return this.i$(a,b.at,b)};b.b.g("ArrayTableDataSource.prototype.add",{add:b.Da.prototype.add});b.Da.prototype.at=function(a){this.Sp();var b;b=0>a||a>=this.qa.data.length?null:{data:this.qa.data[a],index:a,key:this.jt(this.qa.data[a])};return new Promise(function(a){a(b)})};b.b.g("ArrayTableDataSource.prototype.at",{at:b.Da.prototype.at});
b.Da.prototype.change=function(a,d){d=d||{};this.Sp();var c=d.silent,e,f,h,k,l={data:[],keys:[],indexes:[]};a instanceof Array||(a=[a]);for(e=0;e<a.length;e++)f=a[e],null!=f&&(h=this.jt(f),k=this.Fh(h,null),l.data.push(f),l.keys.push(h),l.indexes.push(k.index),this.qa.data[k.index]=f);!c&&0<l.data.length&&b.T.q.handleEvent.call(this,b.T.D.CHANGE,l);return Promise.resolve(l)};b.b.g("ArrayTableDataSource.prototype.change",{change:b.Da.prototype.change});b.Da.prototype.fetch=function(a){a=a||{};return"init"!=
a.fetchType||this.Vx?this.De(a):Promise.resolve()};b.b.g("ArrayTableDataSource.prototype.fetch",{fetch:b.Da.prototype.fetch});b.Da.prototype.get=function(a,b){b=b||{};this.Sp();return Promise.resolve(this.Fh(a,b))};b.b.g("ArrayTableDataSource.prototype.get",{get:b.Da.prototype.get});b.Da.prototype.getCapability=function(){return"full"};b.b.g("ArrayTableDataSource.prototype.getCapability",{getCapability:b.Da.prototype.getCapability});b.Da.prototype.remove=function(a,b){b=b||{};this.Sp();return this.Kq(a,
b)};b.b.g("ArrayTableDataSource.prototype.remove",{remove:b.Da.prototype.remove});b.Da.prototype.reset=function(a,d){d=d||{};d.previousRows=this.qa;var c=d.silent;null!=a&&(this.i=a);this.qa={};this.ke=0;c||b.T.q.handleEvent.call(this,b.T.D.RESET,null);return Promise.resolve()};b.b.g("ArrayTableDataSource.prototype.reset",{reset:b.Da.prototype.reset});b.Da.prototype.sort=function(a){if(null==a)return this.comparator=null,Promise.resolve();this.Sp();var d=a.key,c=a.direction,e=null;"ascending"==c?
e=function(a){return f.isFunction(a[d])?a[d]():a[d]}:"descending"==c&&(e=function(a,b){var c,e;f.isFunction(a[d])?(c=a[d](),e=b[d]()):(c=a[d],e=b[d]);return c===e?0:c>e?-1:1});this.comparator=e;this.direction=c;var g=this;return new Promise(function(c){a=a||{};if(g.aC()){var d=g.comparator;g.qa.data.sort(function(a,c){return b.Da.E0(a,c,d,g)});g.xla=!0;var e={header:a.key,direction:a.direction};b.T.q.handleEvent.call(g,b.T.D.SORT,e);c(e)}})};b.b.g("ArrayTableDataSource.prototype.sort",{sort:b.Da.prototype.sort});
b.Da.prototype.totalSize=function(){return this.ke};b.b.g("ArrayTableDataSource.prototype.totalSize",{totalSize:b.Da.prototype.totalSize});b.Da.prototype.i$=function(a,d,c){var e,f;c=c||{};var h=c.silent,k={data:[],keys:[],indexes:[]};a instanceof Array||(a=[a]);null==d||d instanceof Array||(d=[d]);for(c=0;c<a.length;c++)if(f=a[c],null!=f){e=this.jt(f);k.data.push(f);k.keys.push(e);if(!0==this.xla&&0<this.qa.data.length)for(e=0;e<this.qa.data.length;e++)if(0>b.Da.E0(f,this.qa.data[e],this.comparator,
this)){this.qa.data.splice(e,0,f);k.indexes.push(e);break}else{if(e==this.qa.data.length-1){this.qa.data.push(f);k.indexes.push(e+1);break}}else null==d?(this.qa.data.push(f),k.indexes.push(this.qa.data.length-1)):(this.qa.data.splice(d[c],0,f),k.indexes.push(d[c]));this.ke++;this.Ex()}!h&&0<k.data.length&&b.T.q.handleEvent.call(this,b.T.D.ADD,k);return Promise.resolve(k)};b.Da.prototype.Sp=function(){this.eY()||(this.qa=this.qt(this.i),this.ke=this.i.length)};b.Da.prototype.eY=function(){return null==
this.qa||null==this.qa.data?!1:!0};b.Da.prototype.De=function(a){a=a||{};this.Ux(a);this.Sp();var d;try{d=0<a.pageSize?a.pageSize:-1;this.$||(this.$=0);this.$=null==a.startIndex?this.$:a.startIndex;var c=b.Da.FB(this.qa,this.$,d),e=[],f=[],h;for(h=this.$;h<=c;h++)e[h-this.$]=this.qa.data[h],f[h-this.$]=this.jt(this.qa.data[h])}catch(k){return this.ij(a,null,k),Promise.reject(k)}c<this.$&&(this.$=c+1);a.pageSize=d;a.startIndex=this.$;a.refresh=!0;d={data:e,keys:f,startIndex:this.$};this.ij(a,d,null);
return Promise.resolve(d)};b.Da.prototype.Fh=function(a){var b,c,e,g,h=null;for(b=0;b<this.qa.data.length;b++)if(e=this.qa.data[b],void 0!==e)if(g=this.jt(e),f.isArray(g)&&f.isArray(a)){if(g.length==a.length){var k=!0;for(c=0;c<a.length;c++)if(g[c]!=a[c]){k=!1;break}k&&(h={data:e,key:g,index:this.qa.indexes[b]})}}else g==a&&(h={data:e,key:g,index:this.qa.indexes[b]});return h};b.Da.prototype.aC=function(){var a=this.comparator;return void 0!==a&&null!==a};b.Da.prototype.Ex=function(){for(var a=0;a<
this.qa.data.length;a++)this.qa.indexes[a]=a};b.Da.prototype.Kq=function(a,d){var c,e;d=d||{};var f=d.silent,h={data:[],keys:[],indexes:[]};a instanceof Array||(a=[a]);var k=[];for(c=0;c<a.length;c++)e=a[c],null!=e&&(e=this.jt(e),e=this.Fh(e,null),null!=e&&k.push({data:e.data,key:e.key,index:e.index}));k.sort(function(a,b){return a.index-b.index});for(c=0;c<k.length;c++)h.data.push(k[c].data),h.keys.push(k[c].key),h.indexes.push(k[c].index);for(c=h.indexes.length-1;0<=c;c--)this.qa.data.splice(h.indexes[c],
1),this.qa.indexes.splice(h.indexes[c],1),this.ke--,this.Ex();!f&&0<h.data.length&&b.T.q.handleEvent.call(this,b.T.D.REMOVE,h);return Promise.resolve(h)};b.Da.prototype.Ux=function(a){a.silent||b.T.q.handleEvent.call(this,b.T.D.REQUEST,{startIndex:a.startIndex})};b.Da.prototype.ij=function(a,d,c){null!=c?b.T.q.handleEvent.call(this,b.T.D.ERROR,c):a.silent||b.T.q.handleEvent.call(this,b.T.D.SYNC,d)};b.Da.Bl=function(a,b,c){if("descending"==c){if(a<b)return 1;if(b<a)return-1}else{if(a>b)return 1;if(b>
a)return-1}return 0};b.Da.FB=function(a,b,c){var e=a.data.length-1;0<c&&(e=b+c-1,e=e>a.data.length-1?a.data.length-1:e);return e};b.Da.Pn=function(a,b){return f.isFunction(a[b])?a[b]():a[b]};b.Da.prototype.qt=function(a){var b=a.length-1,c={},e,f;c.data=[];c.indexes=[];this.yn=null;for(e=0;e<=b;e++){var h={},k=a[e];for(f in k)k.hasOwnProperty(f)&&(h[f]=k[f],0==e&&(null==this.yn&&(this.yn=[]),this.yn.push(f)));c.data[e]=h;c.indexes[e]=e}return c};b.Da.prototype.jt=function(a){var d,c=this.aJ(a);if(f.isArray(c)){var e;
d=[];for(e=0;e<c.length;e++)if(c[e]in a)d[e]=a[c[e]];else throw a=b.ha.Lb(b.Da.ec._ERR_ARRAY_TABLE_DATASOURCE_IDATTR_NOT_IN_ROW,[c[e]]),Error(a);}else if(c in a)d=a[c];else throw a=b.ha.Lb(b.Da.ec._ERR_ARRAY_TABLE_DATASOURCE_IDATTR_NOT_IN_ROW,[c]),Error(a);return d};b.Da.prototype.aJ=function(a){if(null!=this.gK)return this.gK;if(null==this.yn){this.yn=[];for(var b in a)a.hasOwnProperty(b)&&this.yn.push(b)}return this.yn.hasOwnProperty("id")?"id":this.yn};b.Da.E0=function(a,d,c,e){var g,h;if(f.isFunction(c)){if(1===
c.length){g=c.call(e,a);h=c.call(e,d);a=b.Ea.nd(g)?g.split(","):[g];d=b.Ea.nd(h)?h.split(","):[h];for(c=0;c<a.length;c++)if(g=b.Da.Bl(a[c],d[c],e.direction),0!==g)return g;return 0}return c.call(e,a,d)}if(b.Ea.nd(c)){var k=c.split(",");for(c=0;c<k.length;c++)if(g=b.Da.Pn(a,k[c]),h=b.Da.Pn(d,k[c]),g=b.Da.Bl(g,h,e.direction),0!==g)return g}return 0};b.Da.ec={_INFO_ARRAY_TABLE_DATASOURCE_IDATTR:"idAttribute option has not been specified. Will default to using 'id' if the field exists. If not, will use all the fields.",
_ERR_ARRAY_TABLE_DATASOURCE_IDATTR_NOT_IN_ROW:"Specified idAttribute {0} not in row data. Please ensure all specified idAttribute fields are in the row data or do not specify idAttribute and all fields will be used as id."}});