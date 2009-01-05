package pomodo.models {
  import org.ruboss.models.RubossModel;
  
  [Resource(name="workunits")]
  [Bindable]
  public class Workunit extends RubossModel {
    public static const LABEL:String = "startedOn";
    
    [DateTime]
    public var startedOn:Date;

    [DateTime]
    public var endedOn:Date;
    
    public var workedMilliseconds:Number = 0;

    [Lazy]
    [BelongsTo]
    public var task:Task;

    public function Workunit() {
      super(LABEL);
    }
  }
}
