<!DOCTYPE html>
<!-- saved from url=(0077)https://grayatomhackthongrp5.slack.com/files/UBQHJGM18/FBQ84J5UZ/chisquare.py -->
<html lang="en-US" class="no_touch supports_sticky_position supports_custom_scrollbar supports_line_clamp"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

	
	<script src="./ChiSquare_files/codemirror_lang_python.dd3e2e25db7e7fb868d6.min.js.download"></script><script async="" src="./ChiSquare_files/slack_beacon.5dbbc3dd9f37d8bc2f4e.min.js.download"></script><script>
window.ts_endpoint_url = "https:\/\/slack.com\/beacon\/timing";

(function(e) {
	var n=Date.now?Date.now():+new Date,r=e.performance||{},t=[],a={},i=function(e,n){for(var r=0,a=t.length,i=[];a>r;r++)t[r][e]==n&&i.push(t[r]);return i},o=function(e,n){for(var r,a=t.length;a--;)r=t[a],r.entryType!=e||void 0!==n&&r.name!=n||t.splice(a,1)};r.now||(r.now=r.webkitNow||r.mozNow||r.msNow||function(){return(Date.now?Date.now():+new Date)-n}),r.mark||(r.mark=r.webkitMark||function(e){var n={name:e,entryType:"mark",startTime:r.now(),duration:0};t.push(n),a[e]=n}),r.measure||(r.measure=r.webkitMeasure||function(e,n,r){n=a[n].startTime,r=a[r].startTime,t.push({name:e,entryType:"measure",startTime:n,duration:r-n})}),r.getEntriesByType||(r.getEntriesByType=r.webkitGetEntriesByType||function(e){return i("entryType",e)}),r.getEntriesByName||(r.getEntriesByName=r.webkitGetEntriesByName||function(e){return i("name",e)}),r.clearMarks||(r.clearMarks=r.webkitClearMarks||function(e){o("mark",e)}),r.clearMeasures||(r.clearMeasures=r.webkitClearMeasures||function(e){o("measure",e)}),e.performance=r,"function"==typeof define&&(define.amd||define.ajs)&&define("performance",[],function(){return r}) // eslint-disable-line
})(window);

</script>
<script>


;(function() {



window.TSMark = function(mark_label) {
	if (!window.performance || !window.performance.mark) return;
	performance.mark(mark_label);
};
window.TSMark('start_load');


window.TSMeasureAndBeacon = function(measure_label, start_mark_label) {
	if (start_mark_label === 'start_nav' && window.performance && window.performance.timing) {
		window.TSBeacon(measure_label, (new Date()).getTime() - performance.timing.navigationStart);
		return;
	}
	if (!window.performance || !window.performance.mark || !window.performance.measure) return;
	performance.mark(start_mark_label + '_end');
	try {
		performance.measure(measure_label, start_mark_label, start_mark_label + '_end');
		window.TSBeacon(measure_label, performance.getEntriesByName(measure_label)[0].duration);
	} catch (e) {
		
	}
};


if ('sendBeacon' in navigator) {
	window.TSBeacon = function(label, value) {
		var endpoint_url = window.ts_endpoint_url || 'https://slack.com/beacon/timing';
		navigator.sendBeacon(endpoint_url + '?data=' + encodeURIComponent(label + ':' + value), '');
	};
} else {
	window.TSBeacon = function(label, value) {
		var endpoint_url = window.ts_endpoint_url || 'https://slack.com/beacon/timing';
		(new Image()).src = endpoint_url + '?data=' + encodeURIComponent(label + ':' + value);
	};
}
})();
</script>
 

<script>
window.TSMark('step_load');
</script>	
		<noscript><meta http-equiv="refresh" content="0; URL=/files/UBQHJGM18/FBQ84J5UZ/chisquare.py?nojsmode=1" /></noscript>


		
		<script type="text/javascript">
		if(self!==top)window.document.write("\u003Cstyle>body * {display:none !important;}\u003C\/style>\u003Ca href=\"#\" onclick="+
		"\"top.location.href=window.location.href\" style=\"display:block !important;padding:10px\">Go to Slack.com\u003C\/a>");
						
		(function() {
			var timer;
			if (self !== top) {
				timer = window.setInterval(function() {
					if (window.$) {
						try {
							$('#page').remove();
							$('#client-ui').remove();
							window.TS = null;
							window.clearInterval(timer);
						} catch(e) {}
					}
				}, 200);
			}
		}());
		
		</script>
	

<script>

(function() {


	window.callSlackAPIUnauthed = function(method, args, callback) {
		var timestamp = Date.now() / 1000;  
		var version = (window.TS && TS.boot_data && TS.boot_data.version_uid) ? TS.boot_data.version_uid.substring(0, 8) : 'noversion';
		var url = '/api/' + method + '?_x_id=' + version + '-' + timestamp;

		var req = new XMLHttpRequest();

		req.onreadystatechange = function() {
			if (req.readyState == 4) {
				req.onreadystatechange = null;
				var obj;

				if (req.status == 200 || req.status == 429) {
					try {
						obj = JSON.parse(req.responseText);
					} catch (err) {
						TS.warn(8675309, 'unable to do anything with api rsp');
					}
				}

				obj = obj || {
					ok: false,
				};

				callback(obj.ok, obj, args);
			}
		};

		var async = true;
		req.open('POST', url, async);

		var form_data = new FormData();
		var has_data = false;
		Object.keys(args).forEach(function(k) {
			if (k[0] === '_') return;
			form_data.append(k, args[k]);
			has_data = true;
		});

		if (has_data) {
			req.send(form_data);
		} else {
			req.send();
		}
	};
})();
</script>

	<script type="text/javascript" src="./ChiSquare_files/webpack.manifest.1dc24ebf5724da1753d7.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>

			
	
		<script>
			if (window.location.host == 'slack.com' && window.location.search.indexOf('story') < 0) {
				document.cookie = '__cvo_skip_doc=' + escape(document.URL) + '|' + escape(document.referrer) + ';path=/';
			}
		</script>
	

		<script type="text/javascript">
		
		try {
			if(window.location.hash && !window.location.hash.match(/^(#?[a-zA-Z0-9_]*)$/)) {
				window.location.hash = '';
			}
		} catch(e) {}
		
	</script>

	<script type="text/javascript">
				
			window.optimizely = [];
			window.dataLayer = [];
			window.ga = false;
		
	
				(function(e,c,b,f,d,g,a){e.SlackBeaconObject=d;
		e[d]=e[d]||function(){(e[d].q=e[d].q||[]).push([1*new Date(),arguments])};
		e[d].l=1*new Date();g=c.createElement(b);a=c.getElementsByTagName(b)[0];
		g.async=1;g.src=f;a.parentNode.insertBefore(g,a)
		})(window,document,"script","https://cfr.slack-edge.com/bv1-4/slack_beacon.5dbbc3dd9f37d8bc2f4e.min.js","sb");
		sb('set', 'token', '3307f436963e02d4f9eb85ce5159744c');

					sb('set', 'user_id', "UBRR5HCT0");
							sb('set', 'user_' + "batch", "signup_api");
							sb('set', 'user_' + "created", "2018-07-13");
						sb('set', 'name_tag', "grayatomhackthongrp5" + '/' + "hegdec29");
				sb('track', 'pageview');

		
		function track(a) {
			if(window.ga) ga('send','event','web', a);
			if(window.sb) sb('track', a);
		}
		

	</script>

	

	<meta name="referrer" content="no-referrer">
		<meta name="superfish" content="nofish">

	<script type="text/javascript">


var TS_last_log_date = null;
var TSMakeLogDate = function() {
	var date = new Date();

	var y = date.getFullYear();
	var mo = date.getMonth()+1;
	var d = date.getDate();

	var time = {
	  h: date.getHours(),
	  mi: date.getMinutes(),
	  s: date.getSeconds(),
	  ms: date.getMilliseconds()
	};

	Object.keys(time).map(function(moment, index) {
		if (moment == 'ms') {
			if (time[moment] < 10) {
				time[moment] = time[moment]+'00';
			} else if (time[moment] < 100) {
				time[moment] = time[moment]+'0';
			}
		} else if (time[moment] < 10) {
			time[moment] = '0' + time[moment];
		}
	});

	var str = y + '/' + mo + '/' + d + ' ' + time.h + ':' + time.mi + ':' + time.s + '.' + time.ms;
	if (TS_last_log_date) {
		var diff = date-TS_last_log_date;
		//str+= ' ('+diff+'ms)';
	}
	TS_last_log_date = date;
	return str+' ';
}

</script>



<script type="text/javascript">

	var TSSSB = {
		call: function() {
			return false;
		}
	};

</script>

	<script type="text/javascript">
		
		window.addEventListener('load', function() {
			var was_TS = window.TS;
			delete window.TS;
			if (was_TS) window.TS = was_TS;
		});
	</script>
	        <title>ChiSquare.py | GrayAtomHackThongrp5 Slack</title>
    <meta name="author" content="Slack">
        

	
		
									
	
		
					
	
						
	
	
	
						
	
	
	
	
	
	
		<!-- output_css "sk_adapter" -->
    <link href="./ChiSquare_files/rollup-slack_kit_legacy_adapters.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">

			<!-- output_css "core" -->
    <link href="./ChiSquare_files/rollup-plastic.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">

		<!-- output_css "before_file_pages" -->
    <link href="./ChiSquare_files/codemirror.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">
    <link href="./ChiSquare_files/codemirror_overrides.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">

	<!-- output_css "file_pages" -->
    <link href="./ChiSquare_files/rollup-file_pages.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">

	
			<!-- output_css "modern" -->
    <link href="./ChiSquare_files/modern.vendor.1832f21.min.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">
    <link href="./ChiSquare_files/application.9a75aee.min.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">

	<!-- output_css "slack_kit_helpers" -->
    <link href="./ChiSquare_files/rollup-slack_kit_helpers.css" rel="stylesheet" type="text/css" id="slack_kit_helpers_stylesheet" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">

	<!-- output_css "regular" -->
    <link href="./ChiSquare_files/print.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">
    <link href="./ChiSquare_files/lato-2-compressed.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)">

	

	
	
		<meta name="robots" content="noindex, nofollow">
	

	
<link id="favicon" rel="shortcut icon" href="https://cfr.slack-edge.com/436da/marketing/img/meta/favicon-32.png" sizes="16x16 32x32 48x48" type="image/png">

<link rel="icon" href="https://cfr.slack-edge.com/436da/marketing/img/meta/app-256.png" sizes="256x256" type="image/png">

<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://cfr.slack-edge.com/436da/marketing/img/meta/ios-152.png">
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://cfr.slack-edge.com/436da/marketing/img/meta/ios-144.png">
<link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://cfr.slack-edge.com/436da/marketing/img/meta/ios-120.png">
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://cfr.slack-edge.com/436da/marketing/img/meta/ios-114.png">
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://cfr.slack-edge.com/436da/marketing/img/meta/ios-72.png">
<link rel="apple-touch-icon-precomposed" href="https://cfr.slack-edge.com/436da/marketing/img/meta/ios-57.png">

<meta name="msapplication-TileColor" content="#FFFFFF">
<meta name="msapplication-TileImage" content="https://cfr.slack-edge.com/436da/marketing/img/meta/app-144.png">
	
<style type="text/css"></style><style type="text/css"> @media only screen and (max-height: NaNpx) { nav#api_nav #footer, nav#site_nav #footer { position: relative; bottom: auto; } }
@media only screen and (min-width: 1441px) { body:not(.nav_open) nav#site_nav #footer { position: relative; bottom: auto; } }</style></head>

<body class="light_theme">

		  			<script>
		
			var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
			if (w > 1440) document.querySelector('body').classList.add('widescreen');
		
		</script>
	
  	
	
	

			

<nav id="site_nav" class="">

	<div id="site_nav_contents">

		<div id="user_menu">
			<div id="user_menu_contents">
				<div id="user_menu_avatar">
										<span class="member_image thumb_48" style="background-image: url(&#39;https://secure.gravatar.com/avatar/d901e124cf1a7e01ded90b70623d2756.jpg?s=192&amp;d=https%3A%2F%2Fcfr.slack-edge.com%2F7fa9%2Fimg%2Favatars%2Fava_0023-192.png&#39;)" data-thumb-size="48" data-member-id="UBRR5HCT0"><ts-icon class="member_type_badge member_type_badge_16">
	<!-- Background for icon -->
	<svg class="member_type_badge_background_ra" width="18px" height="18px" viewBox="0 0 18 18" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
		<g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
			<g id="badge_bg" fill="#FFFFFF">
							</g>
		</g>
	</svg>

	<!-- Actual icon -->
	<svg class="member_type_badge_icon" width="18px" height="18px" viewBox="0 0 18 18" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
		<g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
					</g>
	</svg>
</ts-icon></span>
					<span class="member_image thumb_36" style="background-image: url(&#39;https://secure.gravatar.com/avatar/d901e124cf1a7e01ded90b70623d2756.jpg?s=72&amp;d=https%3A%2F%2Fcfr.slack-edge.com%2F3654%2Fimg%2Favatars%2Fava_0023-72.png&#39;)" data-thumb-size="36" data-member-id="UBRR5HCT0"><ts-icon class="member_type_badge member_type_badge_16">
	<!-- Background for icon -->
	<svg class="member_type_badge_background_ra" width="18px" height="18px" viewBox="0 0 18 18" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
		<g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
			<g id="badge_bg" fill="#FFFFFF">
							</g>
		</g>
	</svg>

	<!-- Actual icon -->
	<svg class="member_type_badge_icon" width="18px" height="18px" viewBox="0 0 18 18" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
		<g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
					</g>
	</svg>
</ts-icon></span>
				</div>
				<h3>Signed in as</h3>
				<span id="user_menu_name">Chetan H. Hegde</span>
			</div>
		</div>

		<div class="nav_contents">

			<ul class="primary_nav">
																	<li><a href="https://grayatomhackthongrp5.slack.com/messages" data-qa="app"><i class="ts_icon ts_icon_angle_arrow_up_left"></i>Back to Slack</a></li>
								<li><a href="https://grayatomhackthongrp5.slack.com/home" data-qa="home"><i class="ts_icon ts_icon_home"></i>Home</a></li>
				<li><a href="https://grayatomhackthongrp5.slack.com/account" data-qa="account_profile"><i class="ts_icon ts_icon_user"></i>Account &amp; profile</a></li>
				<li><a href="https://grayatomhackthongrp5.slack.com/apps/manage" data-qa="configure_apps" target="_blank"><i class="ts_icon ts_icon_plug"></i>Configure apps</a></li>
									<li><a href="https://grayatomhackthongrp5.slack.com/files" data-qa="files"><i class="ts_icon ts_icon_all_files"></i>Files</a></li>
				
														<li><a href="https://grayatomhackthongrp5.slack.com/stats" data-qa="statistics"><i class="ts_icon ts_icon_dashboard"></i>Analytics</a></li>
													<li><a href="https://grayatomhackthongrp5.slack.com/customize" data-qa="customize"><i class="ts_icon ts_icon_magic"></i>Customize</a></li>
													<li>
						<a href="https://grayatomhackthongrp5.slack.com/account/workspace-settings" data-qa="team_settings">
							<i class="ts_icon ts_icon_info_circle sk_dark_grey"></i>
							About this workspace						</a>
					</li>
							</ul>
			
		</div>

		<div id="footer">
									<ul id="footer_nav">
				<li><a href="https://grayatomhackthongrp5.slack.com/is" data-qa="tour">Tour</a></li>
				<li><a href="https://grayatomhackthongrp5.slack.com/downloads" data-qa="download_apps">Download apps</a></li>
				<li><a href="https://grayatomhackthongrp5.slack.com/brand-guidelines" data-qa="brand_guidelines">Brand guidelines</a></li>
				<li><a href="https://grayatomhackthongrp5.slack.com/help" data-qa="help">Help</a></li>
				<li><a href="https://api.slack.com/" target="_blank" data-qa="api">API<i class="ts_icon ts_icon_external_link small_left_margin ts_icon_inherit"></i></a></li>
								<li><a href="https://grayatomhackthongrp5.slack.com/pricing?ui_step=96&amp;ui_element=5" data-qa="pricing" data-clog-event="GROWTH_PRICING" data-clog-ui-element="pricing_link" data-clog-ui-action="click" data-clog-ui-step="admin_footer">Pricing</a></li>
				<li><a href="https://grayatomhackthongrp5.slack.com/help/requests/new" data-qa="contact">Contact</a></li>
				<li><a href="https://grayatomhackthongrp5.slack.com/terms-of-service" data-qa="policies">Policies</a></li>
				<li><a href="https://slackhq.com/" target="_blank" data-qa="our_blog">Our blog</a></li>
				<li><a href="https://slack.com/signout/399847770006?crumb=s-1531652361-aa71dfd078f0495901fbe4e8ce2d1f7b01b06bce17da697f5db79176d7c4d643-%E2%98%83" data-qa="sign_out">Sign out<i class="ts_icon ts_icon_sign_out small_left_margin ts_icon_inherit"></i></a></li>
			</ul>

			<p id="footer_signature">Made with <i class="ts_icon ts_icon_heart"></i> by Slack</p>

		</div>
	</div>
</nav>

	
			
<header class="headroom showSearch headroom--top">
			<a id="menu_toggle" class="" data-qa="menu_toggle_hamburger">
			<span class="menu_icon"></span>
			<span class="menu_label">Menu</span>
			<span class="vert_divider"></span>
		</a>
		<h1 id="header_team_name" class="inline_block" data-qa="header_team_name">
			<a href="https://grayatomhackthongrp5.slack.com/home">
				<i class="ts_icon ts_icon_home"></i>
				GrayAtomHackThongrp5
			</a>
		</h1>
		<div class="header_nav">
			<div class="header_btns float_right">
				<a href="https://grayatomhackthongrp5.slack.com/files/UBQHJGM18/FBQ84J5UZ/chisquare.py" onclick="return false;" id="plans_switcher" data-qa="plans_switcher">
					<i class="ts_icon ts_icon_rocket ts_icon_inherit"></i>
					<span class="block label">Plans</span>
				</a>

				<ul id="header_plans_nav" data-qa="plans_switcher_menu">
					<li class="plans_switcher_item " data-plan="learn_more_standard"><a data-clog-event="UPGRDEXP_PLANS_IN_TEAM_NAV" data-clog-ui-element="learn_more_standard" data-clog-ui-action="click" data-clog-ui-step="TEAM_NAV_PLANS_MENU" href="https://slack.com/pricing/standard?ui_element=53&amp;ui_step=222">
						<span class="switcher_label">Standard</span>
					</a></li>
					<li class="plans_switcher_item " data-plan="learn_more_plus"><a data-clog-event="UPGRDEXP_PLANS_IN_TEAM_NAV" data-clog-ui-element="learn_more_plus" data-clog-ui-action="click" data-clog-ui-step="TEAM_NAV_PLANS_MENU" href="https://slack.com/pricing/plus?ui_element=54&amp;ui_step=222">
						<span class="switcher_label">Plus</span>
					</a></li>
					<li class="plans_switcher_item " data-plan="learn_more_enterprise"><a data-clog-event="UPGRDEXP_PLANS_IN_TEAM_NAV" data-clog-ui-element="learn_more_enterprise" data-clog-ui-action="click" data-clog-ui-step="TEAM_NAV_PLANS_MENU" href="https://slack.com/plans/enterprise-grid?ui_element=55&amp;ui_step=222">
						<span class="switcher_label">Enterprise</span>
					</a></li>
					<li class="plans_switcher_item " data-plan="compare_plans"><a data-clog-event="UPGRDEXP_PLANS_IN_TEAM_NAV" data-clog-ui-element="pricing_link" data-clog-ui-action="click" data-clog-ui-step="TEAM_NAV_PLANS_MENU" href="https://slack.com/plans/compare?ui_element=5&amp;ui_step=222">
						<span class="switcher_label">Compare plans</span>
					</a></li>
				</ul>

				<a href="https://grayatomhackthongrp5.slack.com/files/UBQHJGM18/FBQ84J5UZ/chisquare.py" onclick="return false;" id="team_switcher" data-qa="team_switcher">
					<i class="ts_icon ts_icon_th_large ts_icon_inherit"></i>
					<span class="block label">Workspaces</span>
				</a>
				<a href="https://grayatomhackthongrp5.slack.com/help" id="help_link" data-qa="help_link">
					<i class="ts_icon ts_icon_life_ring ts_icon_inherit"></i>
					<span class="block label">Help</span>
				</a>
															<a href="https://grayatomhackthongrp5.slack.com/messages" data-qa="launch">
							<img src="./ChiSquare_files/ios-64.png" srcset="https://cfr.slack-edge.com/66f9/img/icons/ios-32.png 1x, https://cfr.slack-edge.com/66f9/img/icons/ios-64.png 2x" title="Slack" alt="Launch Slack">
							<span class="block label">Launch</span>
						</a>
												</div>
							<ul id="header_team_nav" data-qa="team_switcher_menu">
																		

	
<li class="active">
	<a href="https://grayatomhackthongrp5.slack.com/home" target="https://grayatomhackthongrp5.slack.com/">
					<i class="ts_icon small ts_icon_check_circle_o active_icon s"></i>
							<i class="team_icon small default">G</i>
				<span class="team_name active">GrayAtomHackThongrp5</span>
	</a>
</li>													

	
<li>
	<a href="https://greyatomapril18batch.slack.com/home" target="https://greyatomapril18batch.slack.com/">
							<i class="team_icon small default">G</i>
				<span class="team_name">GreyAtomApril18Batch</span>
	</a>
</li>																<li id="add_team_option"><a href="https://slack.com/signin" target="_blank"><i class="ts_icon ts_icon_plus team_icon small"></i> <span class="switcher_label">Sign in to another workspace …</span></a></li>
				</ul>
					</div>
	
	
	
</header>	
	<div id="page" style="min-height: 621px;">

		<div id="page_contents" data-qa="page_contents" class="">

<p class="print_only">
	<strong>
	
	Created by vishparks on Sunday, July 15, 2018 at 4:27 PM
	</strong><br>
	<span class="subtle_silver break_word">https://grayatomhackthongrp5.slack.com/files/UBQHJGM18/FBQ84J5UZ/chisquare.py</span>
</p>

<div class="file_header_container no_print">


	<div class="flexpane_file_title">
				<a href="https://grayatomhackthongrp5.slack.com/team/UBQHJGM18" class=" member_preview_link member_image thumb_36" data-member-id="UBQHJGM18" data-thumb-size="36" style="background-image: url(&#39;https://ca.slack-edge.com/TBRQXNN06-UBQHJGM18-g30f7f9b747e-48&#39;)" aria-hidden="true" tabindex="-1">	</a>

		<span class="color_UBQHJGM18 color_9f69e7"><a href="https://grayatomhackthongrp5.slack.com/team/UBQHJGM18" class="message_sender color_UBQHJGM18 color_9f69e7 member member_preview_link " data-member-id="UBQHJGM18">vishparks</a></span>


		<span class="title break_word">
				<a href="https://grayatomhackthongrp5.slack.com/files/UBQHJGM18/FBQ84J5UZ/chisquare.py" data-file-id="FBQ84J5UZ" class="">ChiSquare.py</a>

			<span class="no_wrap">
				

<button type="button" data-file-id="FBQ84J5UZ" class="star ts_icon ts_icon_star_o ts_icon_inherit ts_tip_top star_file ts_tip ts_tip_multiline ts_tip_float ts_tip_hidden btn_unstyle">
	<span class="ts_tip_tip">
		<span class="ts_tip_multiline_inner" data-tip-toggle-auto="Unstar this file">Unstar this file</span>
	</span>
</button>
 
			</span>
		</span>


	</div>

 </div>

<div class="alert_container">
		

<div class="file_public_link_shared alert" style="display: none;">
		
	<i class="ts_icon ts_icon_link"></i> Public Link: <a class="file_public_link" href="https://slack-files.com/TBRQXNN06-FBQ84J5UZ-62782a9797" target="new">https://slack-files.com/TBRQXNN06-FBQ84J5UZ-62782a9797</a>
</div></div>

<div id="file_page" class="card top_padding">

	<p class="small subtle_silver no_print meta">
		
		1KB Python snippet created on <span class="date">July 15, 2018</span>.
				This file is private.		<span class="file_share_list"></span>
	</p>

	<a id="file_action_cog" class="action_cog action_cog_snippet float_right no_print">
		<span>Actions </span><i class="ts_icon ts_icon_cog"></i>
	</a>
	<a id="snippet_expand_toggle" class="float_right no_print">
		<i class="ts_icon ts_icon_expand "></i>
		<i class="ts_icon ts_icon_compress hidden"></i>
	</a>

	<div class="large_bottom_margin clearfix">
		<div class="CodeMirror cm-s-default CodeMirror-wrap" style="height: auto;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5px; left: 35px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true" style="bottom: 0px;"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 30px; margin-bottom: -17px; border-right-width: 13px; min-height: 711px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><span><span>​</span>x</span></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 19px;">&nbsp;</div></div><div class="CodeMirror-code" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">pandas</span> <span class="cm-keyword">as</span> <span class="cm-variable">pd</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">numpy</span> <span class="cm-keyword">as</span> <span class="cm-variable">np</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">scipy</span>.<span class="cm-property">stats</span> <span class="cm-keyword">as</span> <span class="cm-variable">stats</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">4</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">scipy</span>.<span class="cm-property">stats</span> <span class="cm-keyword">import</span> <span class="cm-variable">chi2_contingency</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">5</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">6</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-keyword">class</span> <span class="cm-def">ChiSquare</span>:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">7</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp;  <span class="cm-keyword">def</span> <span class="cm-def">__init__</span>(<span class="cm-variable-2">self</span>, <span class="cm-variable">dataframe</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">8</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">df</span> = <span class="cm-variable">dataframe</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">9</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">p</span> = <span class="cm-builtin">None</span> <span class="cm-comment">#P-Value</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">10</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">chi2</span> = <span class="cm-builtin">None</span> <span class="cm-comment">#Chi Test Statistic</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">11</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">dof</span> = <span class="cm-builtin">None</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">12</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  </span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">13</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">dfTabular</span> = <span class="cm-builtin">None</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">14</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">dfExpected</span> = <span class="cm-builtin">None</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">15</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">16</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp;  <span class="cm-keyword">def</span> <span class="cm-def">_print_chisquare_result</span>(<span class="cm-variable-2">self</span>, <span class="cm-variable">colX</span>, <span class="cm-variable">alpha</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">17</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable">result</span> = <span class="cm-string">""</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">18</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-keyword">if</span> <span class="cm-variable-2">self</span>.<span class="cm-property">p</span><span class="cm-operator">&lt;</span><span class="cm-variable">alpha</span>:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">19</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  <span class="cm-variable">result</span>=<span class="cm-string">"{0} is IMPORTANT for Prediction"</span>.<span class="cm-property">format</span>(<span class="cm-variable">colX</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">20</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-keyword">else</span>:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">21</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  <span class="cm-variable">result</span>=<span class="cm-string">"{0} is NOT an important predictor. (Discard {0} from model)"</span>.<span class="cm-property">format</span>(<span class="cm-variable">colX</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">22</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">23</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-keyword">print</span>(<span class="cm-variable">result</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">24</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp;  </span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">25</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp;  <span class="cm-keyword">def</span> <span class="cm-def">TestIndependence</span>(<span class="cm-variable-2">self</span>,<span class="cm-variable">colX</span>,<span class="cm-variable">colY</span>, <span class="cm-variable">alpha</span>=<span class="cm-number">0.05</span>):</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">26</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable">X</span> = <span class="cm-variable-2">self</span>.<span class="cm-property">df</span>[<span class="cm-variable">colX</span>].<span class="cm-property">astype</span>(<span class="cm-builtin">str</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">27</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable">Y</span> = <span class="cm-variable-2">self</span>.<span class="cm-property">df</span>[<span class="cm-variable">colY</span>].<span class="cm-property">astype</span>(<span class="cm-builtin">str</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">28</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  </span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">29</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">dfObserved</span> = <span class="cm-variable">pd</span>.<span class="cm-property">crosstab</span>(<span class="cm-variable">Y</span>,<span class="cm-variable">X</span>) </span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">30</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable">chi2</span>, <span class="cm-variable">p</span>, <span class="cm-variable">dof</span>, <span class="cm-variable">expected</span> = <span class="cm-variable">stats</span>.<span class="cm-property">chi2_contingency</span>(<span class="cm-variable-2">self</span>.<span class="cm-property">dfObserved</span>.<span class="cm-property">values</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">31</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">p</span> = <span class="cm-variable">p</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">32</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">chi2</span> = <span class="cm-variable">chi2</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">33</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">dof</span> = <span class="cm-variable">dof</span> </span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">34</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  </span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">35</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">dfExpected</span> = <span class="cm-variable">pd</span>.<span class="cm-property">DataFrame</span>(<span class="cm-variable">expected</span>, <span class="cm-variable">columns</span>=<span class="cm-variable-2">self</span>.<span class="cm-property">dfObserved</span>.<span class="cm-property">columns</span>, <span class="cm-variable">index</span> = <span class="cm-variable-2">self</span>.<span class="cm-property">dfObserved</span>.<span class="cm-property">index</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">36</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  </span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">37</div></div><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"> &nbsp; &nbsp; &nbsp;  <span class="cm-variable-2">self</span>.<span class="cm-property">_print_chisquare_result</span>(<span class="cm-variable">colX</span>, <span class="cm-variable">alpha</span>)</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 711px;"></div><div class="CodeMirror-gutters" style="height: 724px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 29px;"></div></div></div></div>

		<p class="file_page_meta no_print" style="line-height: 1.5rem;">
			<label class="checkbox normal mini float_right no_top_padding no_min_width">
				<input type="checkbox" id="file_preview_wrap_cb"> wrap long lines			</label>
		</p>

	</div>

			<div id="comments_holder" class="clearfix clear_both">
	<div class="col span_1_of_6"></div>
	<div class="col span_4_of_6 no_right_padding">
		<div id="file_page_comments">
	<div class="file_comments_FBQ84J5UZ comments">
		
	</div>
</div>	
		

	<p class="p-external_file_author_notice hidden">
		
			<strong class="dull_grey">Can’t view comments</strong><br>
			This file is from another workspace.
			</p>

	<form action="https://grayatomhackthongrp5.slack.com/files/UBQHJGM18/FBQ84J5UZ/chisquare.py" id="file_comment_form" class="comment_form clearfix" method="post">
					<a href="https://grayatomhackthongrp5.slack.com/team/UBRR5HCT0" class="member_preview_link" data-member-id="UBRR5HCT0">
				<span class="member_image thumb_36" style="background-image: url(&#39;https://secure.gravatar.com/avatar/d901e124cf1a7e01ded90b70623d2756.jpg?s=72&amp;d=https%3A%2F%2Fcfr.slack-edge.com%2F3654%2Fimg%2Favatars%2Fava_0023-72.png&#39;)" data-thumb-size="36" data-member-id="UBRR5HCT0"><ts-icon class="member_type_badge member_type_badge_16">
	<!-- Background for icon -->
	<svg class="member_type_badge_background_ra" width="18px" height="18px" viewBox="0 0 18 18" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
		<g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
			<g id="badge_bg" fill="#FFFFFF">
							</g>
		</g>
	</svg>

	<!-- Actual icon -->
	<svg class="member_type_badge_icon" width="18px" height="18px" viewBox="0 0 18 18" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
		<g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
					</g>
	</svg>
</ts-icon></span>
			</a>
				<input type="hidden" name="addcomment" value="1">
		<input type="hidden" name="crumb" value="s-1531652361-5be381d2995dcb7bd5dab0baec81168512d7828181ee419b78f87d24de2ce646-☃">

		<div id="file_comment" class="small texty_comment_input comment_input small_bottom_margin texty_legacy ql-container" name="comment" wrap="virtual" style="overflow: hidden;" data-contenteditable-override="true"><div class="ql-editor ql-blank" data-gramm="false" contenteditable="true" role="textbox" tabindex="0" aria-label="Comment" aria-multiline="true" aria-autocomplete="list" aria-expanded="false" aria-owns="chat_input_tab_ui" spellcheck="false"><p><br></p></div><div class="ql-clipboard" contenteditable="true" tabindex="-1" aria-hidden="true" role="presentation" spellcheck="false"></div></div>
		<div class="file_comment_submit_container display_flex justify_content_between">
			<button type="submit" class="file_comment_submit_btn btn align_self_start   ladda-button" data-style="expand-right"><span class="ladda-label">Add Comment</span></button>
			<span class="input_note indifferent_grey file_comment_tip"></span>		</div>
	</form>

<form id="file_edit_comment_form" class="edit_comment_form clearfix hidden" method="post">
		<div id="file_edit_comment" class="small texty_comment_input comment_input small_bottom_margin" name="comment" wrap="virtual"></div>
	<input type="submit" class="save btn float_right " value="Save">
	<button class="cancel btn btn_outline float_right small_right_margin ">Cancel</button>
</form>	
	</div>
	<div class="col span_1_of_6"></div>
</div>	
</div>


	
		
	</div>
	<div id="overlay"></div>
</div>







<script type="text/javascript">

	/**
	 * A placeholder function that the build script uses to
	 * replace file paths with their CDN versions.
	 *
	 * @param {String} file_path - File path
	 * @returns {String}
	 */
	function vvv(file_path) {

		var vvv_warning = 'You cannot use vvv on dynamic values. Please make sure you only pass in static file paths.';
		if (TS && TS.warn) {
			TS.warn(vvv_warning);
		} else {
			console.warn(vvv_warning);
		}

		return file_path;
	}

	var cdn_url = "https:\/\/cfr.slack-edge.com";
	var vvv_abs_url = "https:\/\/slack.com\/";
	var inc_js_setup_data = {
		emoji_sheets: {
			apple: 'https://cfr.slack-edge.com/c00d19/img/emoji_2017_12_06/sheet_apple_64_indexed_256.png',
			google: 'https://cfr.slack-edge.com/c00d19/img/emoji_2017_12_06/sheet_google_64_indexed_256.png',
		},
	};
</script>
	<script type="text/javascript">
<!--
	// common boot_data
	var boot_data = {
		start_ms: Date.now(),
		app: "web",
		user_id: 'UBRR5HCT0',
		team_id: 'TBRQXNN06',
		visitor_uid: ".2clf5aodbh1c08ggg848os4s4",
		no_login: false,
		version_ts: "1531544937",
		version_uid: "21136bed0f59c29e0eba53821e11e99850283a49",
		cache_version: "v16-giraffe",
		cache_ts_version: "v2-bunny",
		redir_domain: "slack-redir.net",
		signin_url: 'https://slack.com/signin',
		abs_root_url: "https:\/\/slack.com\/",
		api_url: '/api/',
		team_url: "https:\/\/grayatomhackthongrp5.slack.com\/",
		image_proxy_url: "https:\/\/slack-imgs.com\/",
		beacon_timing_url: "https:\/\/slack.com\/beacon\/timing",
		beacon_error_url: "https:\/\/slack.com\/beacon\/error",
		clog_url: "clog\/track\/",
		api_token: "xoxs-399847770006-399855590918-398047719393-be3e17cb33",
		ls_disabled: false,
		hc_tracking_qs: "sid=zd-uf-tbrqxnn06-ubrr5hct0",

		vvv_paths: {
			
		lz_string: "https:\/\/cfr.slack-edge.com\/bv1-4\/lz-string-1.4.4.worker.8de1b00d670ff3dc706a0.js",
		codemirror: "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror.min.44a2b0ae2d7a5cac8a95.min.js",
	codemirror_addon_simple: "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_simple.9c76f7896754967b9eda.min.js",
	codemirror_load: "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_load.082b98ffddbb35f246e2.min.js",

	// Silly long list of every possible file that Codemirror might load
	codemirror_files: {
		'apl': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_apl.28ce658730a18a115532.min.js",
		'asciiarmor': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_asciiarmor.b6cae5185b1e92ac1917.min.js",
		'asn.1': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_asn.1.1992736a46ff4b01f93f.min.js",
		'asterisk': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_asterisk.8dc14a25826407ab1fa3.min.js",
		'brainfuck': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_brainfuck.d29773c7ac178228d4c1.min.js",
		'clike': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_clike.cccd21c94a2b7ab7ce3d.min.js",
		'clojure': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_clojure.4a91a0c50a64467f2ff5.min.js",
		'cmake': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_cmake.a873ff1604fb8e89955f.min.js",
		'cobol': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_cobol.2b7098fad4936f18f361.min.js",
		'coffeescript': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_coffeescript.68a8fdd315d0dcf8c27a.min.js",
		'commonlisp': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_commonlisp.879f5b578b25a058fc4d.min.js",
		'css': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_css.035ca224464953138c30.min.js",
		'crystal': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_crystal.79beb330be1a294e43c4.min.js",
		'cypher': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_cypher.525ea24cf7710ac2825a.min.js",
		'd': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_d.7328ff9ab8c98103deb7.min.js",
		'dart': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_dart.f7e22fcf397d31e7af93.min.js",
		'diff': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_diff.c3b6cf00600144071d6d.min.js",
		'django': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_django.cde302c62fe6365529f2.min.js",
		'dockerfile': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_dockerfile.ed0e37e03b2023e1b69b.min.js",
		'dtd': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_dtd.df3795754645134d5f80.min.js",
		'dylan': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_dylan.fed72f1d0e846fd6d213.min.js",
		'ebnf': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_ebnf.6af113fdedf587f96c64.min.js",
		'ecl': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_ecl.12b9206b24a5433649ab.min.js",
		'eiffel': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_eiffel.896ceb473406cc01ee59.min.js",
		'elm': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_elm.637ce7bda68e33c4b55a.min.js",
		'erlang': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_erlang.ea42edc0caacbb7b9429.min.js",
		'factor': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_factor.937f3b4ba675a2abe9c7.min.js",
		'forth': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_forth.89f6ec54d5548d4cf25b.min.js",
		'fortran': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_fortran.e312d7972b690a22beab.min.js",
		'gas': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_gas.abc6e9d7c3a0b887ff69.min.js",
		'gfm': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_gfm.8fc0c8e3735d10a858c6.min.js",
		'gherkin': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_gherkin.9e0cfa25c1965e495419.min.js",
		'go': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_go.5ed96d85ab19d7795ba7.min.js",
		'groovy': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_groovy.c496c31bd5cca0986ead.min.js",
		'haml': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_haml.f25c65cf09f1ec3a29c7.min.js",
		'handlebars': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_handlebars.80eb7b9e2e0fb6dee382.min.js",
		'haskell': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_haskell.e7b2cc288c6bd281ff32.min.js",
		'haxe': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_haxe.3efebdfa3dc7fb7cc4db.min.js",
		'htmlembedded': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_htmlembedded.1a2496c621f9a470c340.min.js",
		'htmlmixed': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_htmlmixed.caa675603dc4fdb90c31.min.js",
		'http': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_http.c1c249d14bf18521fee1.min.js",
		'idl': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_idl.715601d44fbe133c065b.min.js",
		'jade': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_jade.0eff9474d977d43feced.min.js",
		'javascript': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_javascript.bc1b5c6a6515b3064108.min.js",
		'jinja2': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_jinja2.5de8bc52face9b2769f2.min.js",
		'julia': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_julia.32d8748fecc17e6305bf.min.js",
		'livescript': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_livescript.f6dbad1e8d8168b319f4.min.js",
		'lua': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_lua.32780d85e5cbbb59b8eb.min.js",
		'markdown': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_markdown.a7f65f93ece1f31b9e60.min.js",
		'mathematica': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_mathematica.48dd3694f2f71a75544c.min.js",
		'mirc': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_mirc.0f3984162d72c3a0a5ca.min.js",
		'mllike': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_mllike.e4e86126535bd4f7a575.min.js",
		'modelica': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_modelica.d4fd8938619f5c8dc361.min.js",
		'mscgen': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_mscgen.f9d5ab8e95b697c39880.min.js",
		'mumps': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_mumps.b361377133b59678d3d5.min.js",
		'nginx': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_nginx.524bfc39589c37f74bfd.min.js",
		'nsis': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_nsis.b25852c3418f984ae03d.min.js",
		'ntriples': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_ntriples.4e0443a64025c35438a6.min.js",
		'octave': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_octave.3a0c99a5e07bbd9a6d67.min.js",
		'oz': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_oz.e9939d375a47087f59aa.min.js",
		'pascal': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_pascal.f1162aeab4a781363ccd.min.js",
		'pegjs': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_pegjs.7af50308b76ba3251b02.min.js",
		'perl': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_perl.5a7940afe30ba510820a.min.js",
		'php': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_php.64b619fb529d1cd9b781.min.js",
		'pig': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_pig.a30ec6f3ffff33476ac4.min.js",
		'powershell': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_powershell.0ccd1b6a33eb2209c15b.min.js",
		'properties': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_properties.5c0c1436978bf2a7af00.min.js",
		'puppet': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_puppet.53ac0d4fadd68369610e.min.js",
		'python': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_python.dd3e2e25db7e7fb868d6.min.js",
		'q': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_q.4af8c1d9b07ea218977f.min.js",
		'r': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_r.783001720b360a8177a8.min.js",
		'rpm': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_rpm.79678546fb25c75e3208.min.js",
		'rst': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_rst.0fa19c56ae79c0b70c27.min.js",
		'ruby': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_ruby.efce7fd348530776314b.min.js",
		'rust': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_rust.b148ea62a65dfe9f36c0.min.js",
		'sass': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_sass.4e58ddf440975d3864f6.min.js",
		'scheme': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_scheme.52a48304089db7f7708e.min.js",
		'shell': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_shell.8dd47832ce011f080fb8.min.js",
		'sieve': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_sieve.dc92cd9b919e5efb3c05.min.js",
		'slim': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_slim.ba0d300bced932d16420.min.js",
		'smalltalk': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_smalltalk.6dd6e1d419b04500b385.min.js",
		'smarty': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_smarty.428329a9fdb0d8be2a5f.min.js",
		'solr': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_solr.02f1fe78feb4a670b6cc.min.js",
		'soy': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_soy.8145a09e761fee4b0667.min.js",
		'sparql': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_sparql.cf7a2190284c6ca0c11d.min.js",
		'spreadsheet': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_spreadsheet.eeeb35132617f7fa05e6.min.js",
		'sql': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_sql.78a665f0a117e62e46f2.min.js",
		'stex': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_stex.777bff71a93e84be5096.min.js",
		'stylus': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_stylus.6ae0e46fb8c0750c644c.min.js",
		'swift': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_swift.2254c736e8a7f4f51e92.min.js",
		'tcl': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_tcl.13833d90818d7aa20cc6.min.js",
		'textile': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_textile.aa7de5d427d0474f6e14.min.js",
		'tiddlywiki': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_tiddlywiki.efa88c874dc2653bb47e.min.js",
		'tiki': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_tiki.6a8e59872a533ec09dae.min.js",
		'toml': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_toml.4e099e2ec0d834eb7c04.min.js",
		'tornado': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_tornado.feede7e509e683f0998f.min.js",
		'troff': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_troff.d31a17f22f8c679cf3e5.min.js",
		'ttcn': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_ttcn.1bf6637cf05b45897ccd.min.js",
		'ttcn:cfg': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_ttcn-cfg.273e541df1ddc66215ca.min.js",
		'turtle': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_turtle.4cf803c3d74096bfb82a.min.js",
		'twig': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_twig.628d79da0aea153a66fe.min.js",
		'vb': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_vb.828b80361395c4e24aaf.min.js",
		'vbscript': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_vbscript.e19473b2883a8f5e9270.min.js",
		'velocity': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_velocity.09039c2d8f038c5046b2.min.js",
		'verilog': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_verilog.f12abef9991c95696bf5.min.js",
		'vhdl': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_vhdl.6438b130790bb71537f5.min.js",
		'vue': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_vue.b7dca682b49e1cb360cf.min.js",
		'xml': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_xml.c067158d12d43b9b96f7.min.js",
		'xquery': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_xquery.340466967c2bdf65fa66.min.js",
		'yaml': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_yaml.7f71c0f462159ba81033.min.js",
		'z80': "https:\/\/cfr.slack-edge.com\/bv1-4\/codemirror_lang_z80.73d5eb24ebcdece24ced.min.js"
	}		},

		notification_sounds: [{"value":"b2.mp3","label":"Ding","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/b2.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/b2.ogg"},{"value":"animal_stick.mp3","label":"Boing","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/animal_stick.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/animal_stick.ogg"},{"value":"been_tree.mp3","label":"Drop","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/been_tree.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/been_tree.ogg"},{"value":"complete_quest_requirement.mp3","label":"Ta-da","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/complete_quest_requirement.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/complete_quest_requirement.ogg"},{"value":"confirm_delivery.mp3","label":"Plink","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/confirm_delivery.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/confirm_delivery.ogg"},{"value":"flitterbug.mp3","label":"Wow","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/flitterbug.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/flitterbug.ogg"},{"value":"here_you_go_lighter.mp3","label":"Here you go","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/here_you_go_lighter.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/here_you_go_lighter.ogg"},{"value":"hi_flowers_hit.mp3","label":"Hi","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/hi_flowers_hit.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/hi_flowers_hit.ogg"},{"value":"knock_brush.mp3","label":"Knock Brush","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/knock_brush.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/knock_brush.ogg"},{"value":"save_and_checkout.mp3","label":"Whoa!","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/save_and_checkout.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/save_and_checkout.ogg"},{"value":"item_pickup.mp3","label":"Yoink","url":"https:\/\/cfr.slack-edge.com\/7e91\/sounds\/push\/item_pickup.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/item_pickup.ogg"},{"value":"hummus.mp3","label":"Hummus","url":"https:\/\/cfr.slack-edge.com\/7fa9\/sounds\/push\/hummus.mp3","url_ogg":"https:\/\/cfr.slack-edge.com\/46ebb\/sounds\/push\/hummus.ogg"},{"value":"none","label":"None"}],
		alert_sounds: [{"value":"frog.mp3","label":"Frog","url":"https:\/\/slack.global.ssl.fastly.net\/a34a\/sounds\/frog.mp3"}],
		call_sounds: [{"value":"call\/alert_v2.mp3","label":"Alert","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/alert_v2.mp3"},{"value":"call\/incoming_ring_v2.mp3","label":"Incoming ring","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/incoming_ring_v2.mp3"},{"value":"call\/outgoing_ring_v2.mp3","label":"Outgoing ring","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/outgoing_ring_v2.mp3"},{"value":"call\/pop_v2.mp3","label":"Incoming reaction","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/pop_v2.mp3"},{"value":"call\/they_left_call_v2.mp3","label":"They left call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/they_left_call_v2.mp3"},{"value":"call\/you_left_call_v2.mp3","label":"You left call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/you_left_call_v2.mp3"},{"value":"call\/they_joined_call_v2.mp3","label":"They joined call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/they_joined_call_v2.mp3"},{"value":"call\/you_joined_call_v2.mp3","label":"You joined call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/you_joined_call_v2.mp3"},{"value":"call\/confirmation_v2.mp3","label":"Confirmation","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/confirmation_v2.mp3"}],
		call_sounds_version: "v2",
		a11y_sounds: [],
				default_tz: "America\/Los_Angeles",
		
		feature_teambot: false,
		feature_teambot_active: false,
		feature_teambot_view_only_page: false,
		feature_tinyspeck: false,
		feature_create_team_google_auth: false,
		feature_enterprise_custom_tos: true,
		feature_webapp_always_collect_initial_time_period_stats: false,
		feature_search_skip_context: false,
		feature_flannel_use_canary_sometimes: false,
		feature_deprecate_window_cert: true,
		feature_deprecate_window_cert_block: true,
		feature_deprecate_get_member_by_name: false,
		feature_muted_mpim_badging: true,
		feature_modern_process_imsg: true,
		feature_modern_files_info: true,
		feature_message_labels_copy: false,
		feature_slurp_bots: false,
		feature_react_threads: false,
		feature_file_threads: false,
		feature_file_threads_dark_launch: true,
		feature_file_threads_cache_update: false,
		feature_file_threads_local_shares_only: false,
		feature_broadcast_indicator: false,
		feature_subteam_members_diff: true,
		feature_a11y_keyboard_shortcuts: false,
		feature_email_ingestion: false,
		feature_sidebar_context_menu: false,
		feature_attachments_inline: false,
		feature_fix_files: true,
		feature_channel_eventlog_client: true,
		feature_m11n_experiments: true,
		feature_paging_api: false,
		feature_custom_status_expiry: false,
		feature_m11n_custom_status_input: false,
		feature_a11y_custom_status: false,
		feature_better_snooze: false,
		feature_sonic_dnd: true,
		feature_sonic_presence_manager: false,
		feature_sonic_user_groups: false,
		feature_sonic_user_groups_in_sonic: false,
		feature_lazy_user_groups: false,
		feature_pub_to_prv_esc_client: false,
		feature_use_convert_to_private_api: false,
		feature_inform_changes_to_shared_channels_are_workspace_specific: false,
		feature_date_range_exports: true,
		feature_enterprise_app_teams: true,
		feature_enterprise_frecency: true,
		feature_ent_app_management_restriction: false,
		feature_entitlements: true,
		feature_grid_archive_link_fixes: true,
		feature_migration_status_page: true,
		feature_sonic_member_directory: false,
		feature_safeguard_org_retention: true,
		feature_dashboard_sortable_lists: false,
		feature_refactor_admin_stats: false,
		feature_request_signing: true,
		feature_distribute_clone_apps: false,
		feature_leave_workspace_improvements: true,
		feature_enteprise_user_teams_update: true,
		feature_find_your_workspace: true,
		feature_sk_lato_cleanup: false,
		feature_saml_authn_key_expiry_date: true,
		feature_wta_perm_api_split: false,
		feature_wta_client_support: true,
		feature_xoxa_channel_authorization: true,
		feature_wta_optional_ephemeral_message: true,
		feature_wta_conversations_api_channel_created_msg: false,
		feature_file_links_betterer: false,
		feature_enterprise_dm_deeplink: true,
		feature_enterprise_dm_deeplink_copy_update: false,
		feature_session_duration_saved_message: false,
		feature_guest_api_changes: false,
		feature_gdpr_exports: true,
		feature_sso_jit_disabling: true,
		feature_allow_bulk_delete_join_leave_messages: false,
		feature_connecting_shared_channels_enterprise: false,
		feature_shared_channels_enterprise: false,
		feature_snapshots_the_revenge: false,
		feature_mpim_channels: false,
		feature_esc_connected_workspaces_search: false,
		feature_conversations_list: true,
		feature_gdpr_user_join_tos: true,
		feature_user_invite_tos_april_2018: true,
		feature_modernize_invites: false,
		feature_modernize_admin: false,
		feature_admin_in_client: false,
		feature_sonic_whats_new: true,
		feature_winssb_beta_channel: false,
		feature_slack_astronaut_i18n_jpn: true,
		feature_i18n_customer_stories: false,
		feature_cust_acq_i18n_tweaks: false,
		feature_gdpr_website_update: true,
		feature_gdpr_website_fixes: false,
		feature_sales_lp: true,
		feature_presence_sub: true,
		feature_whitelist_zendesk_chat_widget: false,
		feature_live_support_free_plan: false,
		feature_slackbot_goes_to_college: false,
		feature_newxp_enqueue_message: true,
		feature_threads_copy_change: false,
		feature_force_ls_compression: false,
		feature_name_tagging_client: true,
		feature_name_tagging_client_autocomplete: false,
		feature_name_tagging_client_topic_purpose: false,
		feature_use_imgproxy_resizing: true,
		feature_share_mention_comment_cleanup: false,
		feature_external_files: false,
		feature_electron_memory_logging: false,
		feature_native_app_start_non_mac: false,
		feature_app_promo_program: true,
		feature_app_promo_program_expiry_message: false,
		feature_localization_phase_two: false,
		feature_locale_es_LA: false,
		feature_locale_en_GB: false,
		feature_locale_pt_BR: false,
		feature_zero_width_space_word_joiner: true,
		feature_modernize_slash_cmds: false,
		feature_i18n_runtime_translations: true,
		feature_better_join_leave_strings: false,
		feature_channel_exports: false,
		feature_corp_eng_news: false,
		feature_docs: false,
		feature_deprecate_screenhero: true,
		feature_calls_esc_ui: true,
		feature_calls_unsupported_client_strings: false,
		feature_spock_calls: false,
		feature_remote_files_api: false,
		feature_default_shared_channels: true,
		feature_email_notifications_improvements: true,
		feature_react_lfs: false,
		feature_log_quickswitcher_queries: true,
		feature_mc_mentions_tab_prefs_and_channels: false,
		feature_app_permissions_backend_enterprise: true,
		feature_token_ip_whitelist: true,
		feature_rollback_to_mapping: false,
		feature_sidebar_theme_undo: false,
		feature_dont_set_channel_membership_twice: false,
		feature_allow_intra_word_formatting: true,
		feature_allow_cjk_autocomplete: true,
		feature_allow_split_word: false,
		feature_i18n_channels_validate_emoji: true,
		feature_fw_eng_normalization: true,
		feature_slim_scrollbar: false,
		feature_search_query_refinements: true,
		feature_search_spell_corrections: false,
		feature_react_search: true,
		feature_prefs_modernization: false,
		feature_modern_fuzzy_matcher: false,
		feature_sidebar_filters: false,
		feature_sli_channel_archive_suggestions: true,
		feature_sli_channel_search: false,
		feature_sli_user_search: false,
		feature_react_messages: true,
		feature_never_skip_unread_counts: false,
		feature_fetch_missing_channels_in_unread_counts: false,
		feature_m11n_autocomplete_channels: false,
		feature_trim_paragraphs: false,
		feature_member_supermodel: true,
		feature_m11n_autocomplete_members: false,
		feature_hide_unfurl_urls: false,
		feature_react_member_profile_card: false,
		feature_service_import_lfs: false,
		feature_mpdm_default_fe: false,
		feature_channel_notif_dialog_update: false,
		feature_oauth_react_wta: true,
		feature_react_team_picker: true,
		feature_app_index: false,
		feature_app_profile_app_site_link: false,
		feature_custom_app_installs: true,
		feature_gdrive_do_not_install_by_default: true,
		feature_delete_moved_channels: true,
		feature_single_workspace_redirect: true,
		feature_zero_workspace_onboarding: true,
		feature_user_tos: true,
		feature_oom_mv_channels_list: false,
		feature_solr_discoverability: true,
		feature_sso_formatting_error: true,
		feature_single_user_workspace_pagination: true,
		feature_cross_workspace_quick_switcher_prototype: true,
		feature_org_quick_switcher: false,
		feature_ms_latest: true,
		feature_no_preload_video: true,
		feature_guests_use_entitlements: true,
		feature_dlp_ud_users: false,
		feature_emoji_picker_frecently_used: false,
		feature_app_space: true,
		feature_app_space_links: false,
		feature_app_canvases: false,
		feature_attachments_v2: false,
		feature_block_kit_expandable_block: false,
		feature_date_picker: true,
		feature_beacon_js_errors: false,
		feature_http_sendmsg: true,
		feature_app_dialogs_notify_on_cancel: true,
		feature_dialogs_v2_mobile: true,
		feature_user_app_disable_speed_bump: false,
		feature_nudge_team_creators: false,
		feature_onedrive_picker: false,
		feature_lesson_onboarding: true,
		feature_disable_join_notifications: false,
		feature_importer_warnings: false,
		feature_api_admin_page_not_ent: true,
		feature_legacy_cfm: false,
		feature_less_pins: false,
		feature_less_preprocess_fetching: true,
		feature_delete_team_and_apps: true,
		feature_email_forwarding: true,
		feature_pjpeg: false,
		feature_pdf_thumb: true,
		feature_apps_manage_permissions_scope_changes: true,
		feature_app_dir_only_default_true: false,
		feature_reminder_cross_workspace: true,
		feature_speedy_boot_handlebars: false,
		feature_app_profile_card_trigger_shared_channels: false,
		feature_apps_store_m11n: false,
		feature_block_kit_pillow_file: false,
		feature_channel_invite_modal_cannot_join: false,
		feature_expiring_credits: true,
		feature_email_prefs: true,
		feature_checkout_flow_translations: false,
		feature_modernize_banners: true,
		feature_modernize_banners_v2: true,
		feature_modernize_banners_v3: false,
		feature_sonic_i18n: false,
		feature_flannel_channels_v0: true,
		feature_flannel_always_use_canary: false,
		feature_lazy_channels: true,
		feature_lazy_teams: true,
		feature_flannel_as_shared_channels_events_to_org: true,
		feature_flannel_as_duplicate_events_to_org: false,
		feature_global_nav: false,
		feature_message_spacing: false,
		feature_shortcuts_flexpane: true,
		feature_app_directory_home_page_redesign: true,
		feature_hidden_wksp_unfurls: true,
		feature_guest_wksp_unfurls: false,
		feature_workspace_scim_management: false,
		feature_email_previewer: false,
		feature_redux_dev_tools: false,
		feature_unified_member: false,
		feature_turn_mpdm_notifs_on: true,
		feature_browser_dragndrop: false,
		feature_granular_shared_channel_perms: false,
		feature_lazy_channels_11: false,
		feature_macos_disable_hw: true,
		feature_desktop_notifications_2018: false,
		feature_quill_upgrade: true,
		feature_texty_change_queue: true,
		feature_texty_formatting_commands: true,
		feature_send_button_for_everyone: true,
		feature_ally_sounds: false,
		feature_bots_not_members: false,
		feature_wta_user_data_fe: true,
		feature_wta_app_detail_oauth_updates: false,
		feature_wta_org_level_apps: false,
		feature_shortcuts_prompt: true,
		feature_accessible_dialogs: true,
		feature_app_actions: true,
		feature_app_actions_fe: true,
		feature_app_actions_global: false,
		feature_app_actions_fe_refactor: false,
		feature_shared_channel_free_trial_flow: true,
		feature_i18n_compliance_links: false,
		feature_calls_clipboard_broadcasting_optin: true,
		feature_autocomplete_files: true,
		feature_screen_share_needs_aero: false,
		feature_ent_unified_stars: false,
		feature_calls_disable_iss_admin: true,
		feature_in_prod_trials: true,
		feature_gdpr_account_create: false,
		feature_billing_ce_request_last4: true,
		feature_sli_trending_dashboard: false,
		feature_i18n_custom_status: true,
		feature_i18n_select_empty_state_string: false,
		feature_drift_on_plans_page: true,
		feature_accessible_fs_dialogs: true,
		feature_channel_browser_dropdown: true,
		feature_slackday_unsent_msg_sync: false,
		feature_trap_kb_within_fs_modals: true,
		feature_dialog_speedbump: true,
		feature_react_customize_emoji: false,
		feature_modern_image_viewer: true,
		feature_emoji_by_id: true,
		feature_oauth_internal_integration_banner: true,
		feature_labels_for_core_objects: false,
		feature_jump_to_unread_shortcut: true,
		feature_wta_notifications: true,
		feature_refresh_tokens: false,
		feature_video_file_codec_support: false,
		feature_mc_migration_banner: true,
		feature_channel_converted_to_shared_rtm_handler: false,
		feature_history_changed_modern_rtm_handlers: false,
		feature_attachment_text_more: false,
		feature_turn_off_sso_with_email_option: true,
		feature_aria_application_mode: false,
		feature_block_kit_block_action_on_channel_preview: false,
		feature_compliance_to_select_rebrand_mc: true,
		feature_modern_help_modal: false,
		feature_modern_starred_items: false,
		feature_admin_grid_status: false,

	client_logs: {"0":{"numbers":[0],"user_facing":false},"2":{"numbers":[2],"user_facing":false},"4":{"numbers":[4],"user_facing":false},"5":{"numbers":[5],"user_facing":false},"23":{"numbers":[23],"user_facing":false},"sounds":{"name":"sounds","numbers":[37]},"37":{"name":"sounds","numbers":[37],"user_facing":true},"47":{"numbers":[47],"user_facing":false},"48":{"numbers":[48],"user_facing":false},"Message History":{"name":"Message History","numbers":[58]},"58":{"name":"Message History","numbers":[58],"user_facing":true},"67":{"numbers":[67],"user_facing":false},"72":{"numbers":[72],"user_facing":false},"73":{"numbers":[73],"user_facing":false},"82":{"numbers":[82],"user_facing":false},"88":{"numbers":[88],"user_facing":false},"91":{"numbers":[91],"user_facing":false},"93":{"numbers":[93],"user_facing":false},"96":{"numbers":[96],"user_facing":false},"99":{"numbers":[99],"user_facing":false},"Channel Marking (MS)":{"name":"Channel Marking (MS)","numbers":[141]},"141":{"name":"Channel Marking (MS)","numbers":[141],"user_facing":true},"Channel Marking (Client)":{"name":"Channel Marking (Client)","numbers":[142]},"142":{"name":"Channel Marking (Client)","numbers":[142],"user_facing":true},"Close Old IMs (Client)":{"name":"Close Old IMs (Client)","numbers":[221]},"221":{"name":"Close Old IMs (Client)","numbers":[221],"user_facing":true},"365":{"numbers":[365],"user_facing":false},"389":{"numbers":[389],"user_facing":false},"438":{"numbers":[438],"user_facing":false},"444":{"numbers":[444],"user_facing":false},"481":{"numbers":[481],"user_facing":false},"488":{"numbers":[488],"user_facing":false},"529":{"numbers":[529],"user_facing":false},"552":{"numbers":[552],"user_facing":false},"dashboard":{"name":"dashboard","numbers":[666]},"666":{"name":"dashboard","numbers":[666],"user_facing":false},"667":{"numbers":[667],"user_facing":false},"773":{"numbers":[773],"user_facing":false},"777":{"numbers":[777],"user_facing":false},"794":{"numbers":[794],"user_facing":false},"Client Responsiveness":{"name":"Client Responsiveness","user_facing":false,"numbers":[808]},"808":{"name":"Client Responsiveness","user_facing":false,"numbers":[808]},"Message Pane Scrolling":{"name":"Message Pane Scrolling","numbers":[888]},"888":{"name":"Message Pane Scrolling","numbers":[888],"user_facing":true},"Unread banner and divider":{"name":"Unread banner and divider","numbers":[999]},"999":{"name":"Unread banner and divider","numbers":[999],"user_facing":true},"1000":{"numbers":[1000],"user_facing":false},"Duplicate badges (desktop app icons)":{"name":"Duplicate badges (desktop app icons)","numbers":[1701]},"1701":{"name":"Duplicate badges (desktop app icons)","numbers":[1701],"user_facing":true},"Members":{"name":"Members","numbers":[1975]},"1975":{"name":"Members","numbers":[1975],"user_facing":true},"lazy loading":{"name":"lazy loading","numbers":[1989]},"1989":{"name":"lazy loading","numbers":[1989],"user_facing":true},"thin_channel_membership":{"name":"thin_channel_membership","numbers":[1990]},"1990":{"name":"thin_channel_membership","numbers":[1990],"user_facing":true},"stats":{"name":"stats","numbers":[1991]},"1991":{"name":"stats","numbers":[1991],"user_facing":true},"ms":{"name":"ms","numbers":[1996]},"1996":{"name":"ms","numbers":[1996],"user_facing":true},"shared_channels_connection":{"name":"shared_channels_connection","numbers":[1999]},"1999":{"name":"shared_channels_connection","numbers":[1999],"user_facing":false},"dnd":{"name":"dnd","numbers":[2002]},"2002":{"name":"dnd","numbers":[2002],"user_facing":true},"2003":{"numbers":[2003],"user_facing":false},"Threads":{"name":"Threads","numbers":[2004]},"2004":{"name":"Threads","numbers":[2004],"user_facing":true},"2005":{"numbers":[2005],"user_facing":false},"Reactions":{"name":"Reactions","numbers":[2006]},"2006":{"name":"Reactions","numbers":[2006],"user_facing":true},"TSSSB.focusTabAndSwitchToChannel":{"name":"TSSSB.focusTabAndSwitchToChannel","numbers":[2007]},"2007":{"name":"TSSSB.focusTabAndSwitchToChannel","numbers":[2007],"user_facing":false},"Presence Detection":{"name":"Presence Detection","numbers":[2017]},"2017":{"name":"Presence Detection","numbers":[2017],"user_facing":true},"mc_sibs":{"name":"mc_sibs","numbers":[9999]},"9999":{"name":"mc_sibs","numbers":[9999],"user_facing":false},"Member searching":{"name":"Member searching","numbers":[90211]},"90211":{"name":"Member searching","numbers":[90211],"user_facing":true},"98765":{"numbers":[98765],"user_facing":false},"8675309":{"numbers":[8675309],"user_facing":false}},


		img: {
			app_icon: 'https://cfr.slack-edge.com/272a/img/slack_growl_icon.png'
		},
		page_needs_custom_emoji: false,
		page_needs_enterprise: false	};

	
	
	
	
	// i18n locale map (eg: maps Slack `ja-jp` to ZD `ja`)
			boot_data.slack_to_zd_locale = {"en-us":"en-us","fr-fr":"fr-fr","de-de":"de","es-es":"es","ja-jp":"ja"};
	
	// client boot data
		
			boot_data.should_use_flannel = true;
				boot_data.page_has_incomplete_user_model = true;
		boot_data.flannel_server_pool = "random";
		
	
	
	
	
	
								boot_data.experiment_assignments = {"handlebars_from_smarty_perf":{"experiment_id":"46172931351","type":"user","group":"","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"smartybars_perf":{"experiment_id":"77818061717","type":"user","group":"","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"gdrive_1_5_coachmark_experiment":{"experiment_id":"94271365346","type":"user","group":"yes_coach_mark","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"channel_highlights_dark":{"experiment_id":"134435672660","type":"user","group":"control","trigger":"hash_user","log_exposures":true,"exposure_id":399855590918},"channels_history_cache":{"experiment_id":"145699556609","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"ios_offline_read_marking_2":{"experiment_id":"173210517495","type":"user","group":"offline_read_marking_enabled","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"giovanna_test":{"experiment_id":"181800772038","type":"user","group":"","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"rate_limit_login_by_user_email":{"experiment_id":"190131408354","type":"user","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"rate_limit_login_by_ip_and_id":{"experiment_id":"194465508597","type":"user","group":"","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_channel_insights":{"experiment_id":"202656182946","type":"user","group":"sli_channel_insights","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"app_space_coachmark_copy":{"experiment_id":"205900640787","type":"user","group":"version_a","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"calls_min_bandwidth_moar":{"experiment_id":"208184370230","type":"user","group":"bw_1250","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"early_incr_boot":{"experiment_id":"215725968548","type":"user","group":"control","trigger":"hash_user","log_exposures":true,"exposure_id":399855590918},"sli_channel_insights_dark":{"experiment_id":"228821173360","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_search_ranking_files_trained":{"experiment_id":"240703115856","type":"user","group":"trained","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"message_ranking_top_results":{"experiment_id":"249404098640","type":"user","group":"model_7","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"ios_show_join_beta_button":{"experiment_id":"250307167730","type":"user","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"quick_promo_invite_nudge_2":{"experiment_id":"254763892659","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"app_suggest_link_buttons":{"experiment_id":"259586206071","type":"user","group":"link_buttons","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_search_simplify_top_results":{"experiment_id":"261222155988","type":"user","group":"simplify","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"calls_p2p":{"experiment_id":"268736416752","type":"user","group":"enabled","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"unified_autocomplete":{"experiment_id":"270095428551","type":"user","group":"unified","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"email_i18n_reactivation":{"experiment_id":"275337392980","type":"user","group":"control","trigger":"hash_user","log_exposures":true,"exposure_id":399855590918},"email_i18n_reactivation_v2":{"experiment_id":"276058626338","type":"user","group":"treatment","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"onboarding_2_skip":{"experiment_id":"279490891602","type":"user","group":"show_skip","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"autocomplete_files":{"experiment_id":"299214220897","type":"user","group":"experimental","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_channel_archive_suggestions":{"experiment_id":"303678001734","type":"user","group":"sli_channel_archive_suggestions","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"autocomplete_suggestion_length":{"experiment_id":"306300085110","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"calls_create_attach_join":{"experiment_id":"307534845478","type":"user","group":"enabled","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_search_refinements":{"experiment_id":"310733255011","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_search_refinement_query_solr":{"experiment_id":"310853463040","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_search_autocomplete_ranking":{"experiment_id":"314582940432","type":"user","group":"lambda_rank","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"native_app_start":{"experiment_id":"315357962818","type":"user","group":"control","trigger":"hash_user","log_exposures":true,"exposure_id":399855590918},"search_chat_solrcloud_experiment":{"experiment_id":"316326569424","type":"user","group":"solrcloud","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_refinements_low_results":{"experiment_id":"319377370114","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"calls_cmd_tab":{"experiment_id":"320504100865","type":"user","group":"enabled","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"sli_refinements_spell_only":{"experiment_id":"321169193588","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_search_ac_diversify":{"experiment_id":"322522331094","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"solr_cache_team_fq":{"experiment_id":"323429393127","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"search_precache":{"experiment_id":"325778633617","type":"user","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_default_sorting":{"experiment_id":"328562838083","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_fq_terms_query":{"experiment_id":"329956479699","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"calls_gpu_chill":{"experiment_id":"330871370400","type":"user","group":"enabled","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"sli_all_tab":{"experiment_id":"332269941778","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_two_edit_refinements":{"experiment_id":"336506784599","type":"user","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"content_available_for_all":{"experiment_id":"338553402818","type":"user","group":"treatment","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"sli_search_ac_joint_opt":{"experiment_id":"340568042483","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"sli_search_ac_joint_opt_2":{"experiment_id":"353228692231","type":"user","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"search_cjk_3gram_query":{"experiment_id":"373252327281","type":"user","group":"cjk3","trigger":"launch_user","log_exposures":false,"exposure_id":399855590918},"solr_team_pub_filter":{"experiment_id":"374484526976","type":"user","group":"control","trigger":"hash_user","log_exposures":true,"exposure_id":399855590918},"sli_solr_fetch_count":{"experiment_id":"379680392480","type":"user","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"calls_orca_type":{"experiment_id":"380116885063","type":"user","group":"","trigger":"finished","log_exposures":false,"exposure_id":399855590918},"search_no_fetch_context_ids":{"experiment_id":"387799667952","type":"user","group":"control","trigger":"hash_user","log_exposures":true,"exposure_id":399855590918},"social_nudge_v0":{"experiment_id":"57452636336","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"migrate_stats_to_cds":{"experiment_id":"70039090853","type":"team","group":"stats_cds","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"migrate_stats_enable_dark_reads":{"experiment_id":"70047028338","type":"team","group":"stats_mysql_and_cds_dark_reads","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"domain_signup_links_for_mobile":{"experiment_id":"70804845972","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"update_invite_coachmarks_cta":{"experiment_id":"84280109270","type":"team","group":"invite_cm_got_ita","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"google_contacts_invite_existing":{"experiment_id":"93086200404","type":"team","group":"google_contacts","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"google_contacts_invite_new":{"experiment_id":"93096027173","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"app_suggestions_round_2":{"experiment_id":"131240436582","type":"team","group":"no_suggestions","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"email_autocomplete_android":{"experiment_id":"133221212662","type":"team","group":"enabled","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"modal_3_fields":{"experiment_id":"140209149492","type":"team","group":"modal_3_fields","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"modal_3_fields_existing_teams":{"experiment_id":"142775007765","type":"team","group":"modal_3_fields","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"guest_profiles_and_expiration":{"experiment_id":"145034475616","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"exp_thread_at_mention":{"experiment_id":"145686678499","type":"team","group":"autofill","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"exp_threads_everything_pref":{"experiment_id":"152393699186","type":"team","group":"show_banner","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"lib_mentions_match":{"experiment_id":"153633324374","type":"team","group":"trie","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"app_dir_channel_sidebar_cta":{"experiment_id":"159072431845","type":"team","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"rebuild_mention_map_double_write":{"experiment_id":"164525064375","type":"team","group":"yes","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"tell_joiners_about_joiners":{"experiment_id":"164588156482","type":"team","group":"send_joiners_pushes","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"email_joiners_about_joiners":{"experiment_id":"169717077127","type":"team","group":"send_joiners_emails","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"rebuild_mention_map_with_job":{"experiment_id":"174477577986","type":"team","group":"job","trigger":"launch_team","log_exposures":false,"exposure_id":399847770006},"guest_expiration_announcement":{"experiment_id":"175209361220","type":"team","group":"whats_new","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"edit_team_status_presets":{"experiment_id":"176895283504","type":"team","group":"treatment","trigger":"launch_team","log_exposures":false,"exposure_id":399847770006},"calls_interactive_ss":{"experiment_id":"194479526932","type":"team","group":"enabled","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"pricing_page_v2_2_signedin":{"experiment_id":"199590432480","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"slackbot_help_v2_buttons":{"experiment_id":"200318583393","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"instant_invite_link_ios":{"experiment_id":"201626291921","type":"team","group":"enabled","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"feat_onepage_signup_v2":{"experiment_id":"205971003682","type":"team","group":"single_page","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"feat_limit_meters":{"experiment_id":"212162225108","type":"team","group":"show_limit_meters","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"self_serve_invoicing_checkout":{"experiment_id":"222019723543","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"newxp_onboarding_2_0":{"experiment_id":"235196062839","type":"team","group":"treatment","trigger":"launch_team","log_exposures":false,"exposure_id":399847770006},"feat_msg_lim_search":{"experiment_id":"246809624001","type":"team","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"email_app_onboard_all":{"experiment_id":"252073272226","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"email_app_onboard_admins":{"experiment_id":"252209807013","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"shared_channels_trial_flow":{"experiment_id":"257137512243","type":"team","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"newxp_tips_loading_messages":{"experiment_id":"264238720563","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"small_feat_list":{"experiment_id":"264419561860","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"email_slack_certification":{"experiment_id":"265884802150","type":"team","group":"control","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"no_content_avails":{"experiment_id":"272365364819","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"email_post_upgrade_onboard":{"experiment_id":"273987023266","type":"team","group":"control","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"less_android_badges":{"experiment_id":"274765772358","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"replace_billing_link":{"experiment_id":"276628623189","type":"team","group":"has_plans_link","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"apns2":{"experiment_id":"279378859908","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"free_trial_in_prod":{"experiment_id":"281625415173","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"apns2_part_2":{"experiment_id":"283505922689","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"apns_collapse":{"experiment_id":"286616632582","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"install_apps_link":{"experiment_id":"293721709264","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"test_free_trial_in_prod":{"experiment_id":"300479776051","type":"team","group":"banner_and_email","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"self_serve_sfdc_leads":{"experiment_id":"300549613556","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"email_sfmc_team_joiner_welcome":{"experiment_id":"305390696324","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"drift_on_plans_page":{"experiment_id":"312235426720","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"calls_callstats":{"experiment_id":"313435842625","type":"team","group":"disabled","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"approaching_file_limit_banner":{"experiment_id":"331827143204","type":"team","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"calls_p2p_one_on_one_team":{"experiment_id":"342929142581","type":"team","group":"enabled","trigger":"launch_team","log_exposures":false,"exposure_id":399847770006},"sfmc_trial_onboarding":{"experiment_id":"349854899936","type":"team","group":"treatment","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"email_reached_msg_lim":{"experiment_id":"350501017682","type":"team","group":"treatment","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"checkout_detailed_confirm":{"experiment_id":"356768173168","type":"team","group":"control","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"enable_solrjproxy":{"experiment_id":"357738984711","type":"team","group":"solrjproxy","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"approaching_file_limit_banner_v2":{"experiment_id":"359153329456","type":"team","group":"treatment","trigger":"launch_team","log_exposures":false,"exposure_id":399847770006},"new_dunning_notifs":{"experiment_id":"365025249184","type":"team","group":"treatment","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"logged_in_standard_page_2":{"experiment_id":"367507733044","type":"team","group":"control","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"sfmc_actions_announcement":{"experiment_id":"373115816290","type":"team","group":"treatment","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"search_cjk_3gram_index":{"experiment_id":"374842853543","type":"team","group":"cjk3","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"sfmc_onboarding_webinar":{"experiment_id":"384659518992","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"monetization_no_flannel_login":{"experiment_id":"390413163412","type":"team","group":"fast","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"sfmc_connectingtools_webinar":{"experiment_id":"391331103233","type":"team","group":"treatment","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006},"search_test_exp_2":{"experiment_id":"394969365857","type":"team","group":"","trigger":"finished","log_exposures":false,"exposure_id":399847770006},"search_improvements":{"experiment_id":"396534667719","type":"team","group":"search_improvements","trigger":"hash_team","log_exposures":true,"exposure_id":399847770006}};
			
	// inline_emoji
	boot_data.pref_emoji_mode = "default";
	boot_data.pref_jumbomoji = 1;
	boot_data.pref_messages_theme = "default";

//-->
</script>







	<!-- output_js "libs" -->
<script type="text/javascript" src="./ChiSquare_files/rollup-core_required_libs.eb77e435d1ecfa8fa776.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>

	<!-- output_js "application" -->
<script type="text/javascript" src="./ChiSquare_files/modern.vendor.39fbea4e2bdf3a08a48f.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/application.1617ba6fe88a969dc1ff.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>

	<!-- output_js "page" -->

					<!-- output_js "core" -->
<script type="text/javascript" src="./ChiSquare_files/rollup-core_required_ts.bf7bc07bef495affc5e2.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/TS.web.90a3674f39470d443610.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>

	<!-- output_js "core_web" -->
<script type="text/javascript" src="./ChiSquare_files/rollup-core_web.b0a520c1bd3aa44e07e6.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>

	<!-- output_js "secondary" -->
<script type="text/javascript" src="./ChiSquare_files/TS.web.emoji.269141db2fed71cfc2b6.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/rollup-secondary_a_required.ad92a568b0b3bce22d7e.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/rollup-secondary_b_required.5dcb36fbab107674669e.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>

					
	
	<script type="text/javascript">TS.boot(boot_data);</script>

	<!-- output_js "regular" -->
<script type="text/javascript" src="./ChiSquare_files/TS.web.team_site_nav.47fb3ef7859e7a69378e.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/TS.web.comments.2f314ecb86c10551568f.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/TS.web.file.48cf6ad5ebc46ab6b908.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/codemirror.min.44a2b0ae2d7a5cac8a95.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/codemirror_simple.9c76f7896754967b9eda.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="./ChiSquare_files/codemirror_load.082b98ffddbb35f246e2.min.js.download" crossorigin="anonymous" onload="window._cdn &amp;&amp; _cdn.ok(this, arguments)" onerror="window._cdn &amp;&amp; _cdn.failed(this, arguments)"></script>


			<script type="text/javascript">
	<!--
		boot_data.page_needs_custom_emoji = true;

		boot_data.file = {"id":"FBQ84J5UZ","created":1531652220,"timestamp":1531652220,"name":"ChiSquare.py","title":"ChiSquare.py","mimetype":"text\/plain","filetype":"python","pretty_type":"Python","user":"UBQHJGM18","editable":true,"size":1206,"mode":"snippet","is_external":false,"external_type":"","is_public":false,"public_url_shared":false,"display_as_bot":false,"username":"","url_private":"https:\/\/files.slack.com\/files-pri\/TBRQXNN06-FBQ84J5UZ\/chisquare.py","url_private_download":"https:\/\/files.slack.com\/files-pri\/TBRQXNN06-FBQ84J5UZ\/download\/chisquare.py","permalink":"https:\/\/grayatomhackthongrp5.slack.com\/files\/UBQHJGM18\/FBQ84J5UZ\/chisquare.py","permalink_public":"https:\/\/slack-files.com\/TBRQXNN06-FBQ84J5UZ-62782a9797","edit_link":"https:\/\/grayatomhackthongrp5.slack.com\/files\/UBQHJGM18\/FBQ84J5UZ\/chisquare.py\/edit","preview":"import pandas as pd\r\nimport numpy as np\r\nimport scipy.stats as stats\r\nfrom scipy.stats import chi2_contingency\r\n\r","preview_highlight":"\u003Cdiv class=\"CodeMirror cm-s-default CodeMirrorServer\" oncopy=\"if(event.clipboardData){event.clipboardData.setData('text\/plain',window.getSelection().toString().replace(\/\\u200b\/g,''));event.preventDefault();event.stopPropagation();}\"\u003E\n\u003Cdiv class=\"CodeMirror-code\"\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Epandas\u003C\/span\u003E \u003Cspan class=\"cm-keyword\"\u003Eas\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Epd\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Enumpy\u003C\/span\u003E \u003Cspan class=\"cm-keyword\"\u003Eas\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Enp\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Escipy\u003C\/span\u003E.\u003Cspan class=\"cm-property\"\u003Estats\u003C\/span\u003E \u003Cspan class=\"cm-keyword\"\u003Eas\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Estats\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003Cdiv\u003E\u003Cpre\u003E\u003Cspan class=\"cm-keyword\"\u003Efrom\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Escipy\u003C\/span\u003E.\u003Cspan class=\"cm-property\"\u003Estats\u003C\/span\u003E \u003Cspan class=\"cm-keyword\"\u003Eimport\u003C\/span\u003E \u003Cspan class=\"cm-variable\"\u003Echi2_contingency\u003C\/span\u003E\u003C\/pre\u003E\u003C\/div\u003E\n\u003Cdiv\u003E\u003Cpre\u003E&#8203;\u003C\/pre\u003E\u003C\/div\u003E\n\u003C\/div\u003E\n\u003C\/div\u003E\n","lines":37,"lines_more":32,"preview_is_truncated":true,"channels":[],"groups":[],"ims":["DBRR5HEMU"],"comments_count":0};
		boot_data.file.comments = [];

		

		var g_editor;

		var code_wrap_long_lines = true;

		$(function(){

			var wrap_long_lines = !!code_wrap_long_lines;

			g_editor = CodeMirror(function(elt){
				var content = document.getElementById("file_contents");
				content.parentNode.replaceChild(elt, content);
			}, {
				value: $('#file_contents').text(),
				lineNumbers: true,
				matchBrackets: true,
				indentUnit: 4,
				indentWithTabs: true,
				enterMode: "keep",
				tabMode: "shift",
				viewportMargin: 10,
				readOnly: true,
				lineWrapping: wrap_long_lines
			});

			// past a certain point, CodeMirror rendering may simply stop working.
			// start having CodeMirror use its Long List View-style scolling at >= max_lines.
			var max_lines = 8192;

			var snippet_lines;

			// determine # of lines, limit height accordingly
			if (g_editor.doc && g_editor.doc.lineCount) {
				snippet_lines = parseInt(g_editor.doc.lineCount());
				var new_height;
				if (snippet_lines) {
					// we want the CodeMirror container to collapse around short snippets.
					// however, we want to let it auto-expand only up to a limit, at which point
					// we specify a fixed height so CM can display huge snippets without dying.
					// this is because CodeMirror works nicely with no height set, but doesn't
					// scale (big file performance issue), and doesn't work with min/max-height -
					// so at some point, we have to set an absolute height to kick it into its
					// smart / partial "Long List View"-style rendering mode.
					if (snippet_lines < max_lines) {
						new_height = 'auto';
					} else {
						new_height = (max_lines * 0.875) + 'rem'; // line-to-rem ratio
					}
					var line_count = Math.min(snippet_lines, max_lines);
					TS.info('Applying height of ' + new_height + ' to container for this snippet of ' + snippet_lines + (snippet_lines === 1 ? ' line' : ' lines'));
					$('#page .CodeMirror').height(new_height);
				}
			}

			$('#file_preview_wrap_cb').bind('change', function(e) {
				code_wrap_long_lines = $(this).prop('checked');
				g_editor.setOption('lineWrapping', code_wrap_long_lines);
			})

			$('#file_preview_wrap_cb').prop('checked', wrap_long_lines);

			CodeMirror.switchSlackMode(g_editor, "python");
		});

		
		$('#file_comment').css('overflow', 'hidden').autogrow();
	//-->
	</script>


<style>.color_9f69e7:not(.nuc) {color:#9F69E7;}.color_4bbe2e:not(.nuc) {color:#4BBE2E;}.color_e7392d:not(.nuc) {color:#E7392D;}.color_3c989f:not(.nuc) {color:#3C989F;}.color_674b1b:not(.nuc) {color:#674B1B;}.color_e96699:not(.nuc) {color:#E96699;}.color_e0a729:not(.nuc) {color:#E0A729;}.color_684b6c:not(.nuc) {color:#684B6C;}.color_5b89d5:not(.nuc) {color:#5B89D5;}.color_2b6836:not(.nuc) {color:#2B6836;}.color_99a949:not(.nuc) {color:#99A949;}.color_df3dc0:not(.nuc) {color:#DF3DC0;}.color_4cc091:not(.nuc) {color:#4CC091;}.color_9b3b45:not(.nuc) {color:#9B3B45;}.color_d58247:not(.nuc) {color:#D58247;}.color_bb86b7:not(.nuc) {color:#BB86B7;}.color_5a4592:not(.nuc) {color:#5A4592;}.color_db3150:not(.nuc) {color:#DB3150;}.color_235e5b:not(.nuc) {color:#235E5B;}.color_9e3997:not(.nuc) {color:#9E3997;}.color_53b759:not(.nuc) {color:#53B759;}.color_c386df:not(.nuc) {color:#C386DF;}.color_385a86:not(.nuc) {color:#385A86;}.color_a63024:not(.nuc) {color:#A63024;}.color_5870dd:not(.nuc) {color:#5870DD;}.color_ea2977:not(.nuc) {color:#EA2977;}.color_50a0cf:not(.nuc) {color:#50A0CF;}.color_d55aef:not(.nuc) {color:#D55AEF;}.color_d1707d:not(.nuc) {color:#D1707D;}.color_43761b:not(.nuc) {color:#43761B;}.color_e06b56:not(.nuc) {color:#E06B56;}.color_8f4a2b:not(.nuc) {color:#8F4A2B;}.color_902d59:not(.nuc) {color:#902D59;}.color_de5f24:not(.nuc) {color:#DE5F24;}.color_a2a5dc:not(.nuc) {color:#A2A5DC;}.color_827327:not(.nuc) {color:#827327;}.color_3c8c69:not(.nuc) {color:#3C8C69;}.color_8d4b84:not(.nuc) {color:#8D4B84;}.color_84b22f:not(.nuc) {color:#84B22F;}.color_4ec0d6:not(.nuc) {color:#4EC0D6;}.color_e23f99:not(.nuc) {color:#E23F99;}.color_e475df:not(.nuc) {color:#E475DF;}.color_619a4f:not(.nuc) {color:#619A4F;}.color_a72f79:not(.nuc) {color:#A72F79;}.color_7d414c:not(.nuc) {color:#7D414C;}.color_aba727:not(.nuc) {color:#ABA727;}.color_965d1b:not(.nuc) {color:#965D1B;}.color_4d5e26:not(.nuc) {color:#4D5E26;}.color_dd8527:not(.nuc) {color:#DD8527;}.color_bd9336:not(.nuc) {color:#BD9336;}.color_e85d72:not(.nuc) {color:#E85D72;}.color_dc7dbb:not(.nuc) {color:#DC7DBB;}.color_bc3663:not(.nuc) {color:#BC3663;}.color_9d8eee:not(.nuc) {color:#9D8EEE;}.color_8469bc:not(.nuc) {color:#8469BC;}.color_73769d:not(.nuc) {color:#73769D;}.color_b14cbc:not(.nuc) {color:#B14CBC;}</style>

<!-- slack-www-hhvm-023b3ace5fe756a9b / 2018-07-15 03:59:21 / v21136bed0f59c29e0eba53821e11e99850283a49 / B:H -->



<div id="aria_live_announcer" role="status"></div></body></html>