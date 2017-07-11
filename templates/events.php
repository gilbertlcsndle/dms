<?php
include '../config.php';
include '../timezone.php';
session_start();

include "auth.php";
$loguser=$_SESSION['usn'];

?>
<!DOCTYPE html>
<html lang="en">
<?php include 'header.php'; ?>
<!-- FullCalendar -->
    <link href="../js/fullcalendar/dist/fullcalendar.min.css" rel="stylesheet">
    <link href="../js/fullcalendar/dist/fullcalendar.print.css" rel="stylesheet" media="print">
<style>
	#link{
	font-weight:bold;
	color:#2e8ece;
	text-decoration: underline;	
	}
</style>

  <body class="nav-md">
    <div class="container body">
      <div class="main_container">
        
      <?php include 'headermain.php'; ?>
       <!-- page content -->
        <div class="right_col" role="main">
          <div class="">
            <div class="page-title">
              <div class="title_left">
                <h3>Calendar <small>Click to add/edit events</small></h3>
              </div>

              <div class="title_right">
                <div class="col-md-5 col-sm-5 col-xs-12 form-group pull-right top_search">
              
                </div>
              </div>
            </div>

            <div class="clearfix"></div>

            <div class="row">
              <div class="col-md-12">
                <div class="x_panel">
                  <div class="x_title">
                    <h2>Calendar Events <small>Sessions</small></h2>
                    <ul class="nav navbar-right panel_toolbox">
                    <li style="margin-left:20px"><a class="collapse-link"><i class="fa fa-chevron-up"></i></a>
                    </li>
                    
                    <li><a class="close-link"><i class="fa fa-close"></i></a>
                    </li>
                  </ul>
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">

                    <div id='calendar'></div>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- /page content -->

       <?php include 'footer.php'; ?>
      </div>
    </div>
    <!-- calendar modal -->
    <div id="CalenderModalNew" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">

          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel">New Calendar Entry</h4>
          </div>
          <div class="modal-body">
            <div id="testmodal" style="padding: 5px 20px;">
              <form id="antoform" class="form-horizontal calender" role="form">
                <div class="form-group">
                  <label class="col-sm-3 control-label">Title</label>
                  <div class="col-sm-9">
                    <input type="text" class="form-control" id="title" name="e_title">
                  </div>
                </div>
                <div class="form-group">
                  <label class="col-sm-3 control-label">Description</label>
                  <div class="col-sm-9">
                    <textarea class="form-control" style="height:55px;" id="descr" name="e_des"></textarea>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default antoclose" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary antosubmit">Save changes</button>
          </div>
        </div>
      </div>
    </div>

    <div id="CalenderModalEdit" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">

          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h4 class="modal-title" id="myModalLabel2">Edit Calendar Entry</h4>
          </div>
          <div class="modal-body">

            <div id="testmodal2" style="padding: 5px 20px;">
              <form id="antoform2" class="form-horizontal calender" role="form">
                <div class="form-group">
                  <label class="col-sm-3 control-label">Title</label>
                  <div class="col-sm-9">
                    <input type="hidden" class="form-control" id="e_id" name="e_id">
                    <input type="text" class="form-control" id="title2" name="e_title">
                  </div>
                </div>
                <div class="form-group">
                  <label class="col-sm-3 control-label">Description</label>
                  <div class="col-sm-9">
                    <textarea class="form-control" style="height:55px;" id="descr2" name="e_des"></textarea>
                  </div>
                </div>

              </form>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default del">Delete</button>
            <button type="button" class="btn btn-default antoclose2" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary antosubmit2">Save changes</button>
          </div>
        </div>
      </div>
    </div>

    <div id="fc_create" data-toggle="modal" data-target="#CalenderModalNew"></div>
    <div id="fc_edit" data-toggle="modal" data-target="#CalenderModalEdit"></div>
    <!-- /calendar modal -->

    <?php include 'incfoot.php'; ?>
     <!-- FullCalendar -->
    <script src="../js/fullcalendar/dist/fullcalendar.min.js"></script>
    <!-- FullCalendar -->
    <script>
      $(window).load(function() {
        var date = new Date(),
            d = date.getDate(),
            m = date.getMonth(),
            y = date.getFullYear(),
            started,
            categoryClass;

        var calendar = $('#calendar').fullCalendar({
          header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
          },
          selectable: true,
          selectHelper: true,
          select: function(start, end, allDay) {
            $('#fc_create').click();

            var start=moment(start).format('YYYY-MM-DD');
            var end=moment(end).format('YYYY-MM-DD');

            if(end == start){
            	alert("wow");
            }else{
            $(".antosubmit").one("click", function() {
              var title = $("#title").val();
              var descr = $("#descr").val();

             $.ajax({
				      type:'POST',
				      url:'saveevent.php',
				      data:{title:title,descr:descr,start:start,end:end},
				      success: function(data){
					    calendar.fullCalendar('unselect');
 					    $('.antoclose').click();
              window.location = "events.php";
				      }
			        });
             
            });

        	}
          },
          eventClick: function(calEvent, jsEvent, view) {
            $('#fc_edit').click();
            $('#e_id').val(calEvent.e_id);
            $('#title2').val(calEvent.title);
            $('#descr2').val(calEvent.description);

            //categoryClass = $("#event_type").val();

            $(".del").on("click", function() {
               var e_id = $("#e_id").val();
               if (confirm("Are you sure to delete this event?")) {
                    $.ajax({
                    type:'POST',
                    url:'delevent.php',
                    data:{e_id:e_id},
                    success: function(data){
                    calendar.fullCalendar('unselect');
                    $('.antoclose2').click();
                    window.location = "events.php";
                    }
                    });
               }
            });

            $(".antosubmit2").on("click", function() {
              var title = $("#title2").val();
              var descr = $("#descr2").val();
              var e_id = $("#e_id").val();

              $.ajax({
              type:'POST',
              url:'updateevent.php',
              data:{title:title,descr:descr,e_id:e_id},
              success: function(data){
              calendar.fullCalendar('unselect');
              $('.antoclose2').click();
              window.location = "events.php";
              }
              });
              //calendar.fullCalendar('updateEvent', calEvent);
            });

            //calendar.fullCalendar('unselect');
          },
          eventDrop: function(event, delta,revertFunc) {
          var start= event.start.format('YYYY-MM-DD');
          var end= event.end.format('YYYY-MM-DD');
          var e_id = event.e_id;
          
          //alert(event.title + " was dropped on " + event.start.format());

          if (confirm("Are you sure about this change?")) {
              $.ajax({
              type:'POST',
              url:'updateevendate.php',
              data:{start:start,end:end,e_id:e_id},
              success: function(data){
              calendar.fullCalendar('unselect');
              window.location = "events.php";
              }
              });
          }else{
              revertFunc();
          }

          },eventResize: function(event, delta, revertFunc) {
               var start= event.start.format('YYYY-MM-DD');
               var end= event.end.format('YYYY-MM-DD');
               var e_id = event.e_id;
              //alert(event.title + " end is now " +  = event.end.format());

              if (confirm("Are you sure about this change?")) {
                  $.ajax({
                  type:'POST',
                  url:'updateevendate.php',
                  data:{start:start,end:end,e_id:e_id},
                  success: function(data){
                  calendar.fullCalendar('unselect');
                  window.location = "events.php";
                  }
                  });
              }else{
                  revertFunc();
              }

          },
          editable: true,
          events: [
          <?php 
          $stmt->close();
    		  $stmt=$conn->prepare("select * from tbl_events");
    		  $stmt->execute();
    		  $res=$stmt->get_result();
    		  while($row=$res->fetch_array()){
          ?>
          {
            title: 'Title: <?php echo $row['e_title']; ?>',
            description: '<?php echo $row['e_des']; ?>',
            start: '<?php echo $row['e_start']; ?>',
            end: '<?php echo $row['e_end']; ?>',
            e_id: '<?php echo $row['e_id']; ?>',
          },
          <?php } ?>
          ], eventRender: function(event, element) {
            $(element).tooltip({title: event.description}); 
            element.find('.fc-title').append('<div class="hr-line-solid-no-margin"></div><span style="font-size: 10px">Description: '+event.description+'</span></div>');
        }
        });
      });
    </script>
    <!-- /FullCalendar -->

  </body>
</html>
